"""This is a `Fabric`_ script that helps automate tasks performed while
developing and delivering the course.

.. _Fabric: http://www.fabfile.org/

Invoke it with the :command:`fab` command.
"""

import os
import os.path

# TODO: Look at using docker-fabric in place of directly using
# docker-py. It seems like it would help manage remote docker
# instances through the Fabric SSH tunnels instead of needing to set
# up a CA, create client and server certs, etc.
from docker import Client

from fabric.api import *
from fabric.colors import red


# TODO: Create some tasks that enable the user to manage the classroom
# environment on AWS using boto.


def topdir():
    """Returns the directory where the fabfile is located"""
    return os.path.dirname(env.real_fabfile)


@task
def virtualenv_install():
    """Install/upgrade the virtual environment"""
    if None == os.environ.get('VIRTUAL_ENV'):
        abort(red("VIRTUAL_ENV variable missing from environment. Are you in an active virtualenv?"))
    with lcd(topdir()):
        local("pip install --upgrade -r requirements.txt")


@task
def docs_build():
    """Build a local copy of the documentation"""
    with lcd(os.path.join(topdir(), 'docs')):
        local("make html")


@task
def docs_show():
    """Show the local copy of the documentation in a browser"""
    # Make sure the docs are built
    docs_build()

    # Launch a browser.
    # TODO: Add some code to do the right thing on operating systems other than Ubuntu/Debian
    with lcd(topdir()):
        local("sensible-browser docs/_build/html/index.html")


def student_env_container(base_url=None):
    """Return the docker.container of the first Docker instance that is
    hosting the python-minecraft student environment. Returns None if
    none are found.

    """

    cli = Client(base_url)
    for container in cli.containers():
        if container['Image'].startswith(u'coderdojotc/python-minecraft-student'):
            return container

    return None


@task
def env_sync():
    """Synchronize local source files with those in the environment

    This will copy files into and out of the environment."""

    print(red("Use the Unison keyboard interface to specify which files to sync"))
    container = student_env_container()
    with lcd(topdir()):
        local("docker exec -it {Id} sync-notebooks.sh".format(**container))
    # TODO: Would be nice to figure out why this returns an exit code
    # of 1, prompting warnings from local().


@task
def env_up():
    """Start up the environment"""
    with lcd(topdir()):
        local("vagrant up --provider=docker")


@task
def env_down():
    """Stop the environment"""
    with lcd(topdir()):
        local("vagrant halt")


@task
def env_destroy():
    """Destroy the environment"""
    with lcd(topdir()):
        local("vagrant destroy")

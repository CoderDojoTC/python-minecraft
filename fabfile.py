"""This is a `Fabric`_ script that helps automate tasks performed while
developing and delivering the course.

.. _Fabric: http://www.fabfile.org/

Invoke it with the :command:`fab` command.
"""

# TODO: Look at using docker-fabric in place of directly using
# docker-py. It seems like it would help manage remote docker
# instances through the Fabric SSH tunnels instead of needing to set
# up a CA, create client and server certs, etc.
from docker import Client

from fabric.api import *
from fabric.colors import red


# TODO: Create some tasks that enable the user to manage the classroom
# environment on AWS using boto.


@task
def docs_build():
    """Build a local copy of the documentation"""
    with lcd('docs'):
        local("make html")


@task
def docs_show():
    """Show the local copy of the documentation in a browser"""
    # Make sure the docs are built
    docs_build()

    # Launch a browser.
    # TODO: Add some code to do the right thing on operating systems other than Ubuntu/Debian
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
    local("docker exec -it {Id} sync-notebooks.sh".format(**container))
    # TODO: Would be nice to figure out why this returns an exit code
    # of 1, prompting warnings from local().


@task
def env_up():
    """Start up the environment"""
    local("vagrant up --provider=docker")


@task
def env_down():
    """Stop the environment"""
    local("vagrant halt")


@task
def env_destroy():
    """Destroy the environment"""
    local("vagrant destroy")

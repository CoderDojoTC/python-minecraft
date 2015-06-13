"""This is a `Fabric`_ script that helps automate tasks performed while
developing and delivering the course.

.. _Fabric: http://www.fabfile.org/

Invoke it with the :command:`fab` command.
"""

from docker import Client
from fabric.api import *


@task
def docs_build():
    """ Build a local copy of the documentation
    """
    with lcd('docs'):
        local("make html")


@task
def docs_show():
    """ Show the local copy of the documentation
    """
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

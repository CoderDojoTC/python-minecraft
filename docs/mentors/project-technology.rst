====================
 Project Technology
====================

In the very barest of sketches, this document lays out the different
technologies and resources used for the Python Minecraft :term:`code
group`.


Technologies
============

IPython
-------

The interface to Python used by the students during our workshop is
the `IPython Notebook`_. The Python code is embedded in IPython
Notebook files, which are the files named :file:`*.ipynb` in the
source code repository.

The IPython project hosts an `online notebook viewer`_ that can turn
these ``ipynb`` files into easily readable versions. Just paste any
URL from a GitHub file into the box on the NBViewer site, and  and you will
it will generate a linkable `result like this one`_.

.. _IPython Notebook: http://ipython.org/ipython-doc/stable/notebook/index.html
.. _online notebook viewer: http://nbviewer.ipython.org
.. _result like this one: http://nbviewer.ipython.org/github/CoderDojoTC/python-minecraft/blob/master/Exercise%20%201%20--%20Hello%20World.ipynb


Online Resources
================

Source Code Repository
----------------------

Our `code repository`_ lives on GitHub. This repository is the master
source for the documents, code examples, and scripts and tools used to
support the class.

We try to follow the *feature branch workflow* in our Git
repository. Atlassian provides a `nice overview`_ of this workflow.

.. _code repository: https://github.com/CoderDojoTC/python-minecraft
.. _nice overview: https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow


Mailing Lists
-------------

Our `mailing list`_ is hosted on Google Groups. It is a public group,
open to all.

.. _mailing list: https://groups.google.com/a/coderdojotc.org/forum/?hl=en#!forum/group-python


Project Documentation
---------------------

The source code for our documentation is in the `code repository`_. A
readable, online version is available in our project's `Read the Docs
site`_. Any changes to tracked branches in the repository (especially
``master``) will result in the project documentation being rebuilt so
they are current. The Read the Docs `project page`_ is the
administrative interface for this online version.

.. _Read the Docs site: http://coderdojotc.readthedocs.org/projects/python-minecraft/en/latest/
.. _project page: https://readthedocs.org/projects/python-minecraft/


Docker Hub
----------

We use Docker Hub to host a public repository that contains the
`student image`_ used on the lab server for each student. These images
are built using the :file:`Dockerfile` contained in
:file:`lab-server/student-env-image` of our source code
repository. Once built, they are pushed to the Docker Hub so they can
be retrieved by anyone hosting a lab server, or by students using
Vagrant to host an environment on their personal computer.

.. _student image: https://registry.hub.docker.com/u/coderdojotc/python-minecraft-student/

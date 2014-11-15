================
 The Lab Server
================

Lots to explain here...


Quick Setup
===========

#. Launch an Ubuntu instance somewhere.

#. Log in and gain root access.

#. Install and configure the essentials::

     sudo apt-get install git-core

     git config --global user.name "Mike McCallister"
     git config --global user.email mike@mccllstr.com

#. Clone our repository::

     git clone git clone git@github.com:mikemccllstr/mikemccllstr-python-minecraft.git python-minecraft
     cd python-minecraft
     git checkout vagrant
     cd lab-server

#. Review the :command:`lab-server-setup.sh` script and tweak if where
   needed, then run it::

     sudo ./lab-server-setup.sh

#. Build the student-env-image::

     cd student-env-image
     sudo docker build -t "coderdojotc.org/python-minecraft-student" .

#. Create a config file for the LSC:

.. code-block:: ini

   [Lab Config Sheet]
   email = mike@mccllstr.com
   password = YOUR_APPLICATION_PASSWORD
   spreadsheet = Lab Server Controller
   worksheet = 2014-11-15

   [Instances]
   instance_data_dir = /mnt
   docker_control_url = unix://var/run/docker.sock
   sourcecode_repo = https://github.com/mikemccllstr/mikemccllstr-python-minecraft.git

#. In a tmux window, start running the lsc command with a watch command::

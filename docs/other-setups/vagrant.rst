=======================================
 Setup for a Vagrant-Based Environment
=======================================

A Vagrant-based environment is the preferred way to replicate our
classroom environment on your home PC. It is relatively easy to
install, especially when compared with installing all the different
software components one-by-one, directly on your PC. It also provides
a consistent working environment, so all our other instructions only
need to be written once, instead of once for each operating
system. Finally, Vagrant-based environments are becoming more and more
common in professional software development organizations, so becoming
familiar with this technology will serve students well in the future.


Resulting Environment
=====================

Once you are done following these instructions, you will have a
:term:`command line` tool provided by Vagrant. Using Vagrant, you will
be able to create a lab environment inside a virtual machine running
on your PC. This environment will behave just like the one we use in
the CoderDojo classrooms, so you will be able to follow along with all
the examples.


Installation Steps
==================

These steps outline the tasks you need to perform to be able to use
our Vagrant-based lab environment.


Step 1: Install Vagrant
-----------------------

Vagrant is free, open source software from HashiCorp that helps
recreate development environments from a simple set of instructions
that Vagrant understands. A development environment is a computer
setup where authors of software have all the tools they need to write,
test, and run their software.

Vagrant can be downloaded for Windows, Mac, and Linux from `the
Vagrant website`_. Visit the website, then click on the
:guilabel:`Downloads` link and chose the right version of the software
for your PC's operating system.

Install it like you would any other software.

.. _the Vagrant website: https://www.vagrantup.com/

You can check if you have the latest version of the Vagrant software
installed correctly by typing in the following command at a
:term:`command line`::

  vagrant version

It should print output similar to the following::

  Installed Version: 1.7.2
  Latest Version: 1.7.2

  You're running an up-to-date version of Vagrant!


Step 2: Install VirtualBox
--------------------------

VirtualBox is used by Vagrant to host virtual machines that contain
all the pieces of our development environment. A virtual machine is a
simulated computer, running inside your actual computer. Vagrant takes
care of setting up the virtual machine, starting and stopping it, and
destroying it when you no longer need it. But you need to install
VirtualBox yourself before Vagrant can do the rest.

VirtualBox can be downloaded for Windows, Mac, and Linux from `the
VirtualBox website`_. Visit the website, then click on the
:guilabel:`Downloads` link. You want to download the **VirtualBox
platform package** for your PC's operating system.

Install it like you would any other software.

.. _the VirtualBox website: https://www.virtualbox.org/

You can check if you have the latest version of the VirtualBox
software installed correctly by typing in the following command at a
:term:`command line`::

  vboxmanage --version

It should print output similar to the following::

  4.3.20r96996


Step 3: Get a Copy of the python-minecraft Repository
-----------------------------------------------------

The files we use in our CoderDojo workshops are stored on
GitHub. GitHub is organized into *repositories*, and the
`python-minecraft repository`_ contains all the files used for our lab
environment.

.. _python-minecraft repository: https://github.com/CoderDojoTC/python-minecraft/

The simplest way to get a copy of these files is to download `the Zip
file`_ with all the files from the project. Decompress this file into
a place where you can work on the files, such as a folder under your
:file:`My Documents` folder on Windows, or your home folder on
OS X. We will refer to this location as your **working directory**.

.. _the Zip file: https://github.com/CoderDojoTC/python-minecraft/archive/master.zip

Another alternative, if you have installed a version of Git for your
PC, is to clone the repository from GitHub into a working copy on your
PC. The following command, entered at the :term:`command line`, will
create a copy in a folder named :file:`python-minecraft`::

  git clone https://github.com/CoderDojoTC/python-minecraft.git python-minecraft


Using the Environment
=====================

Once you've completed the steps above, you have everything in place.
As mentioned above, Vagrant is the tool that assembles all the pieces
and starts and stops environments. This section describes how to use
it.

All the commands in this section are intended to be typed at a
:term:`command line`. Before continuing, be sure to change to the
appropriate working directory you created with a copy of the
python-minecraft repository. Use the :command:`cd` command as
follows::

  cd python-minecraft


To start your lab environment
-----------------------------

The first step is to configure a file in your :file:`python-minecraft`
folder called :file:`private_config.yaml`. The easiest way to do this
is to open the file named :file:`sample_config.yaml` in a :term:`text
editor` and use the equivalent of :menuselection:`File --> Save As` to
create a copy with the name :file:`private_config.yaml`. Once you've
saved a copy to the new filename, you must edit it to place your
Mojang account name in the appropriate place. You might also want to
replace the default IPython password.

Once the configuration file is in place, start up the environment
using the :command:`vagrant up` command with the argument
:option:`--provider=docker`. Together, the two will read ``vagrant
up --provider=docker``. An example of how this looks on an Ubuntu PC
is as follows:

.. sourcecode:: shell-session

   [user@pc:~/python-minecraft]$ vagrant up --provider=docker
   Bringing machine 'default' up with 'docker' provider...
   ==> default: Creating the container...
       default:   Name: python-minecraft_default_1424041630
       default:  Image: coderdojotc/python-minecraft-student:latest
       default: Volume: /home/user/python-minecraft:/vagrant
       default:   Port: 10443:8888
       default:   Port: 10565:25565
       default:  
       default: Container created: 76984c0ca81b1fd8
   ==> default: Starting container...
   ==> default: Provisioners will not be run since container doesn't support SSH.

.. note:: The first time you execute the :command:`vagrant up` command
          on a PC might take a long time, depending on the speed of
          the computer and the speed of your connection to the
          Internet. It could take tens of minutes, or maybe even an
          hour.

	  Vagrant downloads software from the Internet to create the
          lab server environment. Most of this software is saved on
          your computer, so it should be faster when you start it a
          second time.

After running the above command, you can pick up with the instructions
in :doc:`../classroom/lab-instance`. Since you are running this on
your own PC, you won't have a :term:`lab instance connection
card`. Instead, check the table below for the necessary information:

+---------------+------------------------------------------------------------+
| Information   | Description                                                |
+===============+============================================================+
| Server Name   | In the classroom documentation, wherever it says           |
|               | ``python.coderdojotc.org``, use ``localhost`` instead. The |
|               | name ``localhost`` refers to your PC itself.               |
+---------------+------------------------------------------------------------+
| IPython URL   | For your local environment, your IPython URL is            |
|               | ``https://localhost:10443/``.                              |
+---------------+------------------------------------------------------------+
| IPython       | This is the value you placed in your                       |
| Password      | :file:`private_config.yaml` file. It defaults to           |
|               | ``fooBARbaz``.                                             |
+---------------+------------------------------------------------------------+
| Mojang        | This is the value you placed in your                       |
| Account Name  | :file:`private_config.yaml` file. It should be something   |
|               | like ``coderdojotc01``. It is **not** your email address.  |
+---------------+------------------------------------------------------------+
| Mojang        | For your local environment, this is the value              |
| Server        | ``localhost:10565``.                                       |
| Address       |                                                            |
+---------------+------------------------------------------------------------+


Destroy the virtual machine
---------------------------

To temporarily stop the lab environment, use the :command:`vagrant
halt` command. You can restart the environment later with the
:command:`vagrant up` command.

To shut down the lab environment, permanently releasing the memory and
hard drive space it is using, you use the :command:`vagrant destroy`
command:

.. sourcecode:: shell-session

   [user@pc:~/python-minecraft]$ vagrant destroy
       default: Are you sure you want to destroy the 'default' VM? [y/N] y
   ==> default: Stopping container...
   ==> default: Deleting the container...

Any servers you were running will be stopped and your Minecraft world
will be lost. The files you edited in your working directory will
still be present. And you can always recreate the lab environment
using the :command:`vagrant up` command described above.

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


Install Vagrant
---------------

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


Install VirtualBox
------------------

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


Get a Copy of the python-minecraft Repository
---------------------------------------------

The files we use in our CoderDojo workshops are stored on
GitHub. GitHub is organized into *repositories*, and the
`python-minecraft repository`_ contains all the files used for our lab
environment.

.. _python-minecraft repository: https://github.com/CoderDojoTC/python-minecraft/

The simplest way to get a copy of these files is to download `the Zip
file` with all the files from the project. Decompress this file into a
place where you can work on the files, such as a folder under your
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


To create the virtual machine containing the lab environment
------------------------------------------------------------

Change into the :file:`solo-server` directory with the :command:`cd`
command, and start up the environment using the :command:`vagrant up`
command. An example of how this looks on an Ubuntu PC is as follows:

.. sourcecode:: shell-session

   [user@pc:~/python-minecraft]$ cd solo-server/
   [user@pc:~/python-minecraft/solo-server]$ vagrant up
   Bringing machine 'default' up with 'virtualbox' provider...
   ==> default: Checking if box 'ubuntu/trusty64' is up to date...
   ==> default: Clearing any previously set forwarded ports...
   ==> default: Clearing any previously set network interfaces...
   [ ... snip ... ]
   ==> default: Congratulations! You now have a Vagrant box that is ready to use for
   ==> default: the CoderDojo exercises!
   ==> default:
   ==> default: First, start the servers in the environment by running the following
   ==> default: command:
   ==> default:
   ==> default:     vagrant ssh -c start-env.sh
   ==> default:
   ==> default: Next, start the Minecraft came on your PC. Make a profile that is
   ==> default: compatible with version 1.7.10, and connect to a multiplayer game on
   ==> default: "localhost".
   ==> default:
   ==> default: Finally, start your web browser on your PC and visit the following
   ==> default: URL:
   ==> default:
   ==> default:     https://localhost:8888/
   ==> default:
   ==> default: The password to connect to IPython is:
   ==> default:     Gewapedy

.. warning:: Make note of the password that is printed in the last
	     line of the output above. You will need it to access the
	     IPython environment. It will stay the same until you
	     :command:`vagrant destroy` the environment (see below).

.. note:: The first time you execute the :command:`vagrant up` command
          on a PC might take a long time (tens of minutes, or maybe
          even an hour). Vagrant will go out to the Internet to
          download the software that forms the foundation of the
          environment. One big portion of this is referred to as the
          Vagrant *box*, which is several hundreds megabytes in
          size. Thankfully, this only happens once, as Vagrant saves
          the box file to reuse later.


To start up the lab environment
-------------------------------

You can run commands inside the vagrant environment using the
:command:`vagrant ssh` command. We use this command to run scripts
(small programs) in the environment that do useful work.

To start up the servers in our lab environment, use the
:command:`vagrant ssh -c start-env.sh` command as illustrated below:

.. sourcecode:: shell-session

   [user@pc:~/python-minecraft/solo-server]$ vagrant ssh -c start-env.sh
   grep: /home/vagrant/minecraft_lab/run/eula.txt: No such file or directory
   Please wait while the libraries initialize...
   Starting: CanaryMod 1.7.10-1.1.2
   Canary Path: /home/vagrant/minecraft_lab/bin/CanaryMod-1.7.10-1.1.2.jar & Working From: /home/vagrant/minecraft_lab/run
   Could not find the server configuration at config/server.cfg, creating default.
   Could not find the database configuration at config/db.cfg, creating default.
   Registered xml Database
   Could not find config/ops.cfg. Creating one for you...
   You can now add ops to config/ops.cfg (one per line!). We left you a note.
   Found 1 plugins; total: 1
   [07:14:33] [CanaryMod] [INFO]: Starting: CanaryMod 1.7.10-1.1.2
   [07:14:33] [CanaryMod] [INFO]: Canary Path: /home/vagrant/minecraft_lab/bin/CanaryMod-1.7.10-1.1.2.jar & Working From: /home/vagrant/minecraft_lab/run
   [07:14:33] [CanaryMod] [INFO]: Could not find the server configuration at config/server.cfg, creating default.
   [07:14:33] [CanaryMod] [INFO]: Could not find the database configuration at config/db.cfg, creating default.
   [07:14:34] [CanaryMod] [INFO]: Registered xml Database
   [07:14:34] [CanaryMod] [INFO]: Could not find config/ops.cfg. Creating one for you...
   [07:14:34] [CanaryMod] [INFO]: You can now add ops to config/ops.cfg (one per line!). We left you a note.
   [07:14:34] [CanaryMod] [INFO]: Found 1 plugins; total: 1
   [07:14:34] [net.minecraft.server.dedicated.DedicatedServer] [INFO]: Starting minecraft server version 1.7.10
   [07:14:34] [net.minecraft.server.dedicated.DedicatedServer] [INFO]: Loading properties
   [07:14:34] [net.minecraft.server.ServerEula] [WARN]: Failed to load eula.txt
   [07:14:34] [net.minecraft.server.dedicated.DedicatedServer] [INFO]: You need to agree to the EULA in order to run the server. Go to eula.txt for more info.
   [07:14:34] [net.minecraft.server.MinecraftServer] [INFO]: Stopping server
   [07:14:34] [net.minecraft.server.MinecraftServer] [INFO]: Saving worlds
   [07:14:34] [CanaryMod] [INFO]: Disabling Plugins ...
   > [07:14:34] [net.minecraft.server.MinecraftServer] [INFO]: Stopping server
   [07:14:34] [net.minecraft.server.MinecraftServer] [INFO]: Saving worlds
   [07:14:34] [CanaryMod] [INFO]: Disabling Plugins ...
   Environment started. Use 'attach-env.sh' to connect to the controlling
   terminals. Use 'stop-env.sh' to halt the environment.
   Connection to 127.0.0.1 closed.

Once you have started the virual machine, you can connect to the
IPython notebook server by visiting https://localhost:8888 using your
web browser. You can connect to the Minecraft world running in the
environment by connecting to a server at localhost:25565.

To attach to the console of the CanaryMod server (for example, to make
another player an Op in the world so they can change it), use the
:command:`vagrant ssh -c attach-env.sh` command. You can disconnect
from the console by typing :kbd:`Ctrl-b d`.

.. todo:: Describe more about how to use the console.


Destroy the virual machine
--------------------------

To shut down the lab environment, permanently releasing the memory and
hard drive space it is using, you use the :command:`vagrant destroy`
command:

.. sourcecode:: shell-session

   [user@pc:~/python-minecraft/solo-server]$ vagrant destroy
       default: Are you sure you want to destroy the 'default' VM? [y/N] y
   ==> default: Forcing shutdown of VM...
   ==> default: Destroying VM and associated drives...
   ==> default: Running cleanup tasks for 'shell' provisioner...

Any servers you were running will be stopped and your Minecraft world
will be lost. The files you edited in your working directory will
still be present. And you can always recreate the lab environment
using the :command:`vagrant up` command described above.

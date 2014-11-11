#!/bin/dash -e

# This script sets up a lab server for hosting student environments
# for the python-minecraft code group.
#
# It is intended to be used as a provisioning script by Vagrant.  The
# provided Vagrantfile invokes this script after creating a vanilla
# box running Ubuntu Trusty (14.04 LTS) as its base image.
#
# The resulting box will have:
#
#  * Docker installed. Docker is used for hosting the student
#    environments. You will need to pull in a student image from a
#    Docker registry, or follow the instructions in the
#    :file:`student-env-image` folder to build one locally.
#
#  * The Lab Server Controller and its pre-dependencies will be
#    installed.
#
#  * The :command:`mcrcon` command will be compiled from source and
#    installed so that the Lab Server Controller can send commands to
#    the running Minecraft server instances.

# ----------------------------------------------------------------------------
# Semi-configurable options

LAB_USER=vagrant


# ----------------------------------------------------------------------------
# Add the official Docker repository

apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
echo deb https://get.docker.com/ubuntu docker main >/etc/apt/sources.list.d/docker.list


# ----------------------------------------------------------------------------
# Install pre-dependencies available in Ubuntu itself

apt-get update
apt-get -y upgrade

# Install tools used by this setup script.
#
# `haveged` is used to make sure the box has enough entropy to
# generate good random numbers without stalling.
#
# `apg` is used to generate passwords.
#
# `python-pip` is used to create the environment in which the Lab
# Sever Controller runs.
apt-get -y install apg haveged python-pip


# ----------------------------------------------------------------------------
# Install Docker

apt-get -y install lxc-docker


# ----------------------------------------------------------------------------
# Install the Lab Server Controller

cd /vagrant/controller
pip install -r requirements.txt
pip install -e .

# Install the mcrcon command so we can send commands to the running
# Minecraft servers with RCON.

cd /home/${LAB_USER}
if [ ! -d mcrcon ]; then
    git clone https://github.com/Tiiffi/mcrcon
fi
cd mcrcon
gcc -std=gnu99 -pedantic -Wall -Wextra -O2 -s -o /usr/local/bin/mcrcon mcrcon.c


# ----------------------------------------------------------------------------
# Clean up and exit

# Link the user's bin directory to the /vagrant/user-commands so that
# they will be found in the user's path, and are easy to invoke like:
#    vagrant ssh -c COMMAND
#ln -s /vagrant/user-commands /home/${LAB_USER}/bin

# Fix up permissions
chown -R ${LAB_USER}:${LAB_USER} /home/${LAB_USER}

# Tell the user what to do next.
cat <<EOF
Congratulations! You now have a Vagrant box that is ready to host lab
environments for students to use for the CoderDojo exercises!

First, connect to the server with:

    vagrant ssh

Change into the /vagrant folder, and consult the README.rst:

    less README.rst
EOF

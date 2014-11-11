#!/bin/dash -e

# This script sets up the most basic server environment for exploring
# how to program Minecraft using Python, through the IPython web
# interface.
#
# It is intended to be used as a provisioning script by Vagrant.  The
# provided Vagrantfile invokes this script after creating a vanilla
# box running Ubuntu Trusty (14.04 LTS) as its base image.
#
# The resulting box have the "vagrant" user set up with the CanaryMod
# server, configured with the RaspberryJuice plugin. It will have an
# IPython notebook server instance with the will be The configured
# Vagrant box is designed to support a single person, running the
# Minecraft game client on the same machine as is hosting the Vagrant
# box.

# ----------------------------------------------------------------------------
# Semi-configurable options

LAB_USER=vagrant
MINECRAFT_LAB=/home/${LAB_USER}/minecraft_lab
RASPBERRY_JUICE_VERSION=1.0.2
CODERDOJO_REPO=https://github.com/mikemccllstr/mikemccllstr-python-minecraft.git


# ----------------------------------------------------------------------------
# Install pre-dependencies available in Ubuntu itself

#apt-get update
#apt-get -y upgrade

# Install the JRE used by the CanaryMod server
#apt-get -y install openjdk-7-jre-headless

# Install git, so we can clone copies of repositories we use
#apt-get -y install git-core

# Install the IPython Notebook
#apt-get -y install ipython-notebook

# Install Python libraries that are used by some demos
#apt-get -y install python-imaging python-pygame

# Install tools used by this setup script.
#
# `haveged` is used to make sure the box has enough entropy to
# generate good random numbers without stalling.
#
# `apg` is used to generate passwords.
#apt-get -y install apg haveged

# Make this environment enough like our Vagrant environment so that
# the remainder of this script will run.
adduser ${LAB_USER}
#apt-get -y install curl openssl tmux psmisc


# ----------------------------------------------------------------------------
# Determine a few things

PASSWORD_PLAINTEXT=$(apg -n 1 -m 6 -x 8 -d -M cln -E lI10OS)
PASSWORD_HASH=$(python -c "import IPython.lib.security; print IPython.lib.security.passwd('${PASSWORD_PLAINTEXT}')")


# ----------------------------------------------------------------------------
# Set up the CanaryMod server

mkdir -p ${MINECRAFT_LAB}/bin
mkdir --mode u=rwx,g=rx,o= ${MINECRAFT_LAB}/run
mkdir --mode u=rwx,g=rx,o=rx ${MINECRAFT_LAB}/run/plugins

cd ${MINECRAFT_LAB}/bin
curl --silent --show-error --remote-name --remote-header-name http://canarymod.net/releases/latest-download
cd -


# ----------------------------------------------------------------------------
# Install the RaspberryJuice plugin for CanaryMod

cd ${MINECRAFT_LAB}
git clone https://github.com/martinohanlon/CanaryRaspberryJuice.git
ln -s ${MINECRAFT_LAB}/CanaryRaspberryJuice/jars/canaryraspberryjuice-${RASPBERRY_JUICE_VERSION}.jar run/plugins


# ----------------------------------------------------------------------------
# Clone the CoderDojoTC repository of examples

cd ${MINECRAFT_LAB}
git clone ${CODERDOJO_REPO} python-minecraft


# ----------------------------------------------------------------------------
# Configure the IPython notebook server

su - ${LAB_USER} -c "ipython profile create nbserver --reset"
cd ${MINECRAFT_LAB}
TMP_FILE=$(mktemp --tmpdir=$PWD)
chmod go-rwx ${TMP_FILE}
mv ${TMP_FILE} ipython-cert.pem
openssl req -x509 -subj "/C=US/ST=MN/L=Twin Cities/O=CoderDojoTC/CN=localhost" -nodes -days 365 -newkey rsa:1024 -keyout ipython-cert.pem -out ipython-cert.pem

cat >/home/${LAB_USER}/.ipython/profile_nbserver/ipython_notebook_config.py <<EOF
# Configuration file for ipython-notebook.

c = get_config()

# Notebook config
c.NotebookApp.certfile = u'${PWD}/ipython-cert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'${PASSWORD_HASH}'
c.NotebookApp.port = 8888
EOF


# ----------------------------------------------------------------------------
# Clean up and exit

# Link the user's bin directory to the /vagrant/user-commands so that
# they will be found in the user's path, and are easy to invoke like:
#    vagrant ssh -c COMMAND
ln -s /vagrant/user-commands /home/${LAB_USER}/bin

# Save our settings in a file so they can be accessed by later scripts
TMP_FILE=$(mktemp --tmpdir=${MINECRAFT_LAB})
chmod go-rwx ${TMP_FILE}
mv ${TMP_FILE} ${MINECRAFT_LAB}/settings

cat >>${MINECRAFT_LAB}/settings <<EOF
MINECRAFT_LAB=${MINECRAFT_LAB}
RASPBERRY_JUICE_VERSION=${RASPBERRY_JUICE_VERSION}
LAB_USER=${LAB_USER}
CODERDOJO_REPO=${CODERDOJO_REPO}
PASSWORD_PLAINTEXT=${PASSWORD_PLAINTEXT}
EOF

# Fix up permissions
chown -R ${LAB_USER}:${LAB_USER} ${MINECRAFT_LAB}

# Tell the user what to do next.
cat <<EOF
Congratulations! You now have a Vagrant box that is ready to use for
the CoderDojo exercises!

First, start the servers in the environment by running the following
command:

    vagrant ssh -c start-env.sh

Next, start the Minecraft came on your PC. Make a profile that is
compatible with version 1.7.10, and connect to a multiplayer game on
"localhost".

Finally, start your web browser on your PC and visit the following
URL:

    https://localhost:8888/

The password to connect to IPython is:
    ${PASSWORD_PLAINTEXT}
EOF

#!/bin/dash -e

# This script should be run by a developer who has started the
# instance in Vagrant, made some changes to the IPython exercises or
# examples using the IPython notebook server, and needs to sync those
# changes back to the version-controlled working directory.

# Run this as follows:
#    docker exec --rm -it python-minecraft_default* sync-notebooks.sh

# ----------------------------------------------------------------------------
# Determine a few things

LAB_USER=student
MINECRAFT_LAB=/home/${LAB_USER}/minecraft-lab


# ----------------------------------------------------------------------------
# Copy the necessary files into place

if [ -d ${MINECRAFT_LAB}/notebooks -a -d /vagrant ]; then

    # Sync between the Vagrant-supplied and the instance notebooks.
    unison /vagrant ${MINECRAFT_LAB}/notebooks -ignore 'Path .git' -ignore 'Path .vagrant' -ignore 'Path */.ipynb_checkpoints'
else
    echo "No Vagrant source directory"
    exit
fi

# Fix up permissions
chown -R ${LAB_USER}:${LAB_USER} ${MINECRAFT_LAB}/notebooks
chown -R --reference=/vagrant /vagrant

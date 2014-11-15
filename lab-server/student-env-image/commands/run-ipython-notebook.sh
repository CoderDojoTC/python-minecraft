#!/bin/dash -e

# This script should be run by Supervisor to start up an IPython
# notebook environment to support the python-minecraft lab
# activities. It is configured through environment variables which get
# passed in from the `docker run` command line.

# ----------------------------------------------------------------------------
# Determine a few things

LAB_USER=student
MINECRAFT_LAB=/home/${LAB_USER}/minecraft-lab


# ----------------------------------------------------------------------------
# Configure IPython

# Create the profile and a cert
su - ${LAB_USER} -c "ipython profile create nbserver --reset"

if [ ! -f /home/${LAB_USER}/.ipython/profile_nbserver/ipython-cert.pem ]; then
    cd /home/${LAB_USER}/.ipython/profile_nbserver/
    TMP_FILE=$(mktemp --tmpdir=$PWD)
    chmod go-rwx ${TMP_FILE}
    mv ${TMP_FILE} ipython-cert.pem
    chown ${LAB_USER}:${LAB_USER} ipython-cert.pem
    openssl req -x509 -subj "/C=US/ST=MN/L=Twin Cities/O=CoderDojoTC/CN=localhost" -nodes -days 365 -newkey rsa:1024 -keyout ipython-cert.pem -out ipython-cert.pem
else
    echo ipython-cert.pem already exists, preserving existing file
fi

# Hash the password
PASSWORD_HASH=$(python -c "import IPython.lib.security; print IPython.lib.security.passwd('${STUDENT_PASSWORD}')")

# Create the config file
cat >/home/${LAB_USER}/.ipython/profile_nbserver/ipython_notebook_config.py <<EOF
# Configuration file for ipython-notebook.

c = get_config()

# Notebook config
c.NotebookApp.certfile = u'/home/${LAB_USER}/.ipython/profile_nbserver/ipython-cert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.password = u'${PASSWORD_HASH}'
c.NotebookApp.port = 8888
EOF

# ----------------------------------------------------------------------------
# Copy the necessary files into place

if [ ! -d ${MINECRAFT_LAB}/notebooks ]; then
    mkdir -p ${MINECRAFT_LAB}
    git clone ${CODERDOJO_REPO} ${MINECRAFT_LAB}/notebooks
    # TODO: Replace the above with a sparse checkout of only the needed stuff

    # Fix up permissions
    chown -R ${LAB_USER}:${LAB_USER} ${MINECRAFT_LAB}/notebooks
fi


# ----------------------------------------------------------------------------
# Start the server

cd ${MINECRAFT_LAB}/notebooks
chown -R ${LAB_USER}:${LAB_USER} .
exec su ${LAB_USER} -c "ipython notebook --profile=nbserver"

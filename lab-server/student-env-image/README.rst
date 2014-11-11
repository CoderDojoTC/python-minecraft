===========================================
 Working With Docker Images and Containers
===========================================

Some quick notes so I don't lose this with my command history.

To build the python-minecraft-student image from the docker file::

  sudo docker build -t "coderdojotc.org/python-minecraft-student" .

To start a container running the python-minecraft-student image::

  sudo docker run -P -i -t coderdojotc.org/python-minecraft-student su - vagrant -c /bin/bash

Once at the bash prompt inside the container, issue the
:command:`start-env.sh` command to bring up the Minecraft and IPython
servers.

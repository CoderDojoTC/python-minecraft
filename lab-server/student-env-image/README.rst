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


To Run a Student Instance
=========================

The idiomatic way to configure Docker containers is to pass
environment variables into the :command:`docker run` command. In
practice, this is roughly what will happen to kick off a student
instance:

#. Create a Docker Data Volume Container to hold the student's files::

     mkdir /tmp/student-AAAA-datadir  # Or something more permanent
     sudo docker run -d  --name student-AAAA-data ubuntu:14.04 echo Data-only container for Student AAAA

#. Launch a container based on the student image::

     sudo docker run -d \
         -v /tmp/student-AAAA-datadir:/home/student/minecraft-lab \
         -e "MOJANG_ACCOUNTS=#####" \
         -e "STUDENT_PASSWORD=####" \
         -e "CODERDOJO_REPO=https://github.com/mikemccllstr/mikemccllstr-python-minecraft.git" \
         -e "SERVER_DNS_NAME=____" \
	 -p 10443:8888 -p 10565:25565 \
         coderdojotc.org/python-minecraft-student

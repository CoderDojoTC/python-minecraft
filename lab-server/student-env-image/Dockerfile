# Builds the python-minecraft-student Docker image. Each student will
# get their own container built from this image.

FROM ubuntu:14.04
MAINTAINER Mike McCallister <mike@mccllstr.com>

ADD /vagrant /vagrant

RUN ["/bin/dash", "-e", "/vagrant/server-setup.sh"]

EXPOSE 8888
EXPOSE 25565

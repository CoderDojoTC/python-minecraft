# Builds the python-minecraft-student Docker image. Each student will
# get their own container built from this image.

FROM ubuntu:14.04
MAINTAINER Mike McCallister <mike@mccllstr.com>

# Pull in the components we need from Ubuntu. This is done here
# instead of in the server setup script because it lets Docker take
# advantage of its cache, which greatly speeds up subsequent builds.

RUN apt-get update \
    && apt-get install -y \
        apg \
	curl \
	git-core \
	haveged \
	ipython-notebook \
	openjdk-7-jre-headless \
	openssl \
	psmisc \
	python-imaging \
	python-pygame \
	supervisor \
	tmux \
    && apt-get clean

ADD /vagrant /vagrant

RUN ["/bin/dash", "-e", "/vagrant/server-setup.sh"]

EXPOSE 8888
EXPOSE 25565
EXPOSE 25575

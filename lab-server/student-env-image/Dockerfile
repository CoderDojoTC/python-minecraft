# Builds the python-minecraft-student Docker image. Each student will
# get their own container built from this image.

FROM phusion/baseimage:0.9.16
MAINTAINER Mike McCallister <mike@mccllstr.com>

# ----------------------------------------------------------------------------
# Pull in the components we need from Ubuntu. This is done here
# instead of in the server setup script because it lets Docker take
# advantage of its cache, which greatly speeds up subsequent builds.

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        apg \
        curl \
        git-core \
        haveged \
        ipython-notebook \
        openjdk-7-jre-headless \
        openssl \
        psmisc \
        python-imaging \
        python-pip \
        python-pygame \
        supervisor \
        tmux \
        unison \
        unzip \
        zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Upgrade IPython to get improved usability of the Notebook server
RUN pip install --upgrade jsonschema==2.4.0 tornado==4.0.0 ipython==3.1.0


# ----------------------------------------------------------------------------
# Minor configurations

# Set up Supervisor to run the pieces of the student's environment
COPY minecraft-lab.conf /etc/supervisor/conf.d/minecraft-lab.conf

# Copy our convenience commands into the image
COPY commands/ /usr/local/bin

# Expose the ports for the IPython notebook server and Minecraft
EXPOSE 8888
EXPOSE 25565

# Set the default command when a container is run
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# Set up the student user
RUN ["adduser", "student", "--disabled-password", "--disabled-login", "--gecos", ""]


# ----------------------------------------------------------------------------
# Prepare the image to run the Canary (Minecraft) Server

# Copy the default Canary configuration/files/world into the image

# NOTE: the contents of the following directory can be recreated with
# the following commands:
#
#     rm -rf server-files/*
#     cd server-files
#     java -jar CANARY_JAR_FILE nogui
#
# Then, make the necessary edits by hand. Do this if the Canary
# version moves ahead far enough that we need to create new default
# configuration files.

COPY default-canary-files/ /usr/local/share/default-canary-files/

# Get a copy of the RaspberryJuice plugin from GitHub

ADD https://github.com/martinohanlon/CanaryRaspberryJuice/blob/master/jars/canaryraspberryjuice-1.3.jar?raw=true /usr/local/share/default-canary-files/plugins/

# Download the Canary jar file

#ADD https://ci.visualillusionsent.net/job/CanaryMod/805/artifact/target/CanaryMod-1.8.0-1.2.1-SNAPSHOT-shaded.jar /usr/local/bin/
ADD http://canarymod.net/releases/CanaryMod-1.2.0.jar /usr/local/bin/CanaryMod-1.8.0-1.2.0-shaded.jar

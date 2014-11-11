# Builds a Docker image that is suitable for compiling Canary. This is
# helpful when/if we need to make a local build of Canary.

FROM ubuntu:14.04
MAINTAINER Mike McCallister <mike@mccllstr.com>

# Pull in the components we need from Ubuntu. This is done here
# instead of in the server setup script because it lets Docker take
# advantage of its cache, which greatly speeds up subsequent builds.

RUN apt-get update \
    && apt-get install -y \
	git-core \
	maven \
	openjdk-7-jdk \
    && apt-get clean

# This is intended to be an interactive environment in which you can
# build Canary.
CMD ["bash", "-l"]

=================
 To Build Canary
=================

Create a Docker Data Volume Container to hold our local copy of the
Canary code and built objects::

  mkdir /tmp/canary-build-dir  # Or something more permanent
  sudo docker run -d -v /tmp/canary-build-dir:/canary-build-dir --name canary-build-data ubuntu:14.04 echo Data-only container for building Canary

Build our Docker image::

  sudo docker build -t "canary-builder" .

Launch a container based on the builder image::

  sudo docker run -it --volumes-from canary-build-data canary-builder

Once at the bash prompt inside the container, change to
``/canary-build-dir``, clone the source repos, build, etc.

  cd /canary-build-dir
  git clone https://github.com/CanaryModTeam/CanaryLib.git
  git clone https://github.com/CanaryModTeam/CanaryMod.git
  cd CanaryLib
  mvn package install
  cd ../CanaryMod
  mvn package

.. note:: You can also edit the code in source of the volume
          (:file:`/tmp/canary-build-dir`, in the example above), and
          just use the Docker container for building.

The resulting binary should be in CanaryMod/target.

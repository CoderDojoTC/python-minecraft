===============
 Release Notes
===============

The following changes have been made to the classroom materials over
time. Look for annotated Git tags that match the headings below.


Latest (untagged release)
=========================

* Simplify the generated world in the student lab instance to make it
  better for programming projects. Now, the students are placed in a
  "FLAT" world (no terrain, no biomes, no structures, no mobs, etc.),
  and the weather is clear.

* Upgraded to CanaryRaspberryJuice version 1.2. This added methods
  such as getPlayerId(playerName), getDirection(), getRotation(), and
  getPitch(). This also includes version 1.1, which added various
  entity methods.

* The docs for setting up a local, Vagrant-based lab environment have
  been updated to work much better. It now uses exactly the same
  environment and setup that students get when attending a CoderDojoTC
  event. The solo-server docs and files have been removed.

* The Lab Server Controller now accepts the name of a docker image
  (and version tags) in its configuration file. This makes it possible
  to use different lab images in different environments, which is
  particularly useful in testing a new image before committing to
  using it for a specific CoderDojo event.

* Lots of documentation updates, including new docs for Mentors.


2015-02-07
==========

* The table of contents and navigation between chapters has been
  improved. Some of the section index pages have been improved.

* Improved the layout of the Lab Instance Connection card, and its
  related documentation.

* Some unnecessary documentation files have been removed.


2015-01-24 and Before
=====================

Release notes are unavailable prior to the February 7, 2015
session. Please consult the `git log`_ for details of prior releases.

.. _git log: https://github.com/CoderDojoTC/python-minecraft/commits/master

=======================
 Overview of the Setup
=======================

You need several things to be able to participate in these
activities. This document introduces you to these pieces. The
following pages show you how to set them up for your specific
operating system.

 * `Minecraft`_
 * `CanaryMod Server`_
 * `RaspberryJuice for CanaryMod`_
 * `Git`_
 * `Python`_
 * `A Text Editor`_


Minecraft
=========

This is what you run when you start the game itself. Most of the time,
it is actually the `Minecraft launcher`_, which you have downloaded_
from Mojang. This is sometimes referred to as the *client*, because in
these activities, we will connect it to a separate server that you
will control through Python.

.. _Minecraft launcher: http://minecraft.gamepedia.com/Minecraft_launcher
.. _downloaded: https://minecraft.net/download


CanaryMod Server
================

CanaryMod_ is a Minecraft server_. Like the vanilla Minecraft server
from Mojang itself, it can be used to host a multiplayer_ game of
Minecraft. Unlike the vanilla server, CanaryMod has a plugin API which
allows it to be customized by developers. Unlike the CraftBukkit
server, it is still available to download in both source code and
compiled forms (as of October 2014).

.. _CanaryMod: http://canarymod.net/
.. _server: http://minecraft.gamepedia.com/Server
.. _multiplayer: http://minecraft.gamepedia.com/Multiplayer


RaspberryJuice for CanaryMod
============================

Mojang release a special version of Minecraft (called the `Minecraft:
Pi Edition`_) that runs on a small, inexpensive computer called the
Raspberry Pi. This version of Minecraft is special because it is
available to download and use for no cost, and because it comes with
support for modifying the game server's behavior in multiple
programming languages. The only downside to this special version is
that it **requires** a Raspberry Pi, and cannot be run on a regular
computer. While a Raspberry Pi is relatively inexpensive, most
students probably already have access to a regular computer than can
run the normal version of Minecraft, so we've looked for an
alternative.

The original alternative came from the RaspberryJuice_ plugin for the
CraftBukkit server. This plugin supports the same methods for
customizing the server's behavior as the Minecraft: Pi Edition, but it
can be used with the PC version of Minecraft.

Due to some turmoil in the Bukkit project beginning around early
September 2014, CraftBukkit is unavailable for the time being. The
good news is that the CanaryMod server also has a `plugin equivalent
to RaspberryJuice`_, so it is the one we can use.

.. _`Minecraft: Pi Edition`: http://pi.minecraft.net/
.. _RaspberryJuice: http://dev.bukkit.org/bukkit-plugins/raspberryjuice/
.. _`plugin equivalent to RaspberryJuice`: http://canarymod.net/forum/viewtopic.php?f=33&t=3812


Git
===

Git is a `developer's tool`_ for keeping track of changes made to
files. These kinds of tools are commonly referred to as Version
Control Systems (VCS) or Source Code Management systems (SCM), because
developers use them to keep track of the files that go into the
programs they write. The examples used in the CoderDojo class are kept
in a Git repository, along with the files that make up the
RaspberryJuice plugin.

.. _`developer's tool`: http://git-scm.com/


Python
======

Python is the language in which we will develop our mods for
Minecraft. It is free and open source, it runs on pretty much any
computer around. It is both easy for beginners and powerful enough for
very complicated or sophisticated programs.


A Text Editor
=============

Python programs are written in plain text files. As such, you will
need a program that helps create and update these files. There are
many available, and most computers even come with one out of the
box. However, some editors have features that make it easier to read,
write, and test computer programs, so we will select one of those.

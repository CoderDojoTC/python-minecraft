================
 The Lab Server
================

If you are responsible for running a lab server that hosts multiple
student instances during a CoderDojo session, this is the guide for
you.

This is currently a pretty cursory explanation for how to setup a lab
server from scratch, and then how to operate it during a CoderDojo
session.

.. todo:: Need to elaborate on AWS usage, such as how to create an
          instance, pick the size and availability zone, configure the
          Elastic IP, etc.

In summary, the Lab Server hosts a bunch of Instances. Each student
will get their own Instance. Each Instance hosts a private Minecraft
server, the RaspberryJuice plugin that lets Python talk to Minecraft,
and an IPython Notebook server that can talk to the Minecraft
server. These Instances give each student an isolated environment in
which they can work through lessons and challenges.

To control the instances on the Lab Server, there is a python script
called the Lab Server Controller. It runs on the Lab Server, and it is
responsible for configuring, starting, and stopping individual
Instances. The Lab Server Controller gets its information from the
Control Sheet, which is a Sheet in Google Docs that contains
information about the desired configuration of the various Instances.

While class is in session, Mentors will control the Lab Server and its
instances by making updates to the Control Sheet.


Building the Lab Server AWS Instance
====================================

The following steps are needed to create a new lab server instance
using nothing but a standard Ubuntu 14.04 LTS installation and the
contents of the python-minecraft repository.

#. Launch an Ubuntu instance in AWS.

#. Log in and gain root access.

#. Install and configure the essentials::

     apt-get install git-core

     git config --global user.name "Your Name"
     git config --global user.email youremail@example.com

#. Clone our repository::

     git clone https://github.com/CoderDojoTC/python-minecraft.git python-minecraft
     cd python-minecraft
     cd lab-server

#. Review the :command:`lab-server-setup.sh` script and tweak it where
   needed, then run it::

     ./lab-server-setup.sh

#. Build the student-env-image::

     cd student-env-image
     docker build -t "coderdojotc.org/python-minecraft-student" .


The Lab Server Controller
=========================

The Lab Server Controller is a command line tool that helps manage the
lab server used for teaching the CoderDojo TC's Python-Minecraft code
group.

The Lab Server Controller (LSC, from here) helps manage the
server. The LSC is embodied in a command named :command:`lsc`. This
command provides several different operations, which are basically
subcommands. It can be run interactively for some operations. For
others, it is designed to be run as a scripted tool.

For many operations, the LSC pulls its configuration data from a
Google Sheet that follows a pre-defined format. This Sheet, referred
to from here on as the *Control Sheet*, describes how the containers
should be configured for the students. Keeping this information in a
Google Doc allows it to be easily updated by Mentors in the
classroom. The expected contents are described in detail below in the
section titled `Control Sheet Format`_.


Configuration
-------------

Before you can use the LSC command for the first time, create a file
in your current directory named :file:`lsc.ini`. Populate it with
content like the following:

.. code-block:: ini

   [Lab Config Data]
   email = your-google-account-email@example.com
   password = YOUR_APPLICATION_SPECIFIC_GOOGLE_PASSWORD
   spreadsheet = Lab Server Controller
   worksheet = 2014-11-15

   [Instances]
   instance_data_dir = /mnt
   docker_control_url = unix://var/run/docker.sock
   sourcecode_repo = https://github.com/CoderDojoTC/python-minecraft.git
   docker_image = coderdojotc.org/python-minecraft-student:latest

The ``spreadsheet`` value is the name of the Google Sheet that the LSC
should use for its configuration data. The ``worksheet`` is the name
of the specific tab within the Sheet.

The ``email`` value is the address of the Google Account that the LSC
should use to connect to the Sheet. It will probably be the email
address of the person responsible for setting up and running the
server.

The ``password`` field is the password the LSC should use, in
conjunction with the email address of the Google Account, when
connecting to the Google Sheet. **It is a terrible, terrible idea to
enter your main Google password in this field. Please consult the
warning below for what to do instead.**

.. warning:: Absolutely **everyone** ought to be using Google's
	     `2-factor authentication`_, especially people who need to
	     write down their password in a configuration file.  To
	     make the LSC tool work when you have it set up, you need
	     to create an `application-specific password`_.  The
	     password you set up on that page should be the one you
	     enter in the config file.

.. todo:: Need to document other values in config file above.

.. _`2-factor authentication`: https://support.google.com/accounts/answer/180744?hl=en
.. _`application-specific password`: https://accounts.google.com/b/0/IssuedAuthSubTokens?hl=en&hide_authsub=1


Usage
-----

Normal usage when the lab server is up and running is to log into the
lab server, switch to the root user (who can start and stop Docker
instances), launch a :command:`tmux` session, then start running the
lab server controller in a loop with a command like the following::

  watch -n 10 timeout 60 lsc -v --debug process-commands

If you want to know more about what the :command:`lsc` command can
actually do, this section describes various usage examples. The name
of the command itself is :command:`lsc`. Each of the different
subcommands follows ``lsc`` on the command line.


Environment Shakeout Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commands in this section help with environment shakeout.

The :command:`lsc test` command checks the environment. It confirms
that the config file is present. It validates that the information in
the config file allows it to reach the Control Sheet used to manage
the student instances.


Control Sheet Commands
~~~~~~~~~~~~~~~~~~~~~~

The commands in this section help with managing the Control Sheet.

The :command:`lsc show` command dumps the contents of the Control
Sheet.

The :command:`lsc process-commands` command walks through the Control
Sheet and attempts to act on each command in the sheet, as indicated
in the sheet. It also checks the current state of each instance and
updates the appropriate columns in the Control Sheet.


Control Sheet Format
====================

The LSC expects the Control Sheet to follow a certain format, so it
knows where to find the necessary information. Overall, the first row
in the sheet should contain the column headings listed below. Each row
after that describes an Instance.

Here is how the columns expected to be laid out within the sheet:

Inst #
  This is the numeric identifier of the instance. It should be
  unique. It should be an integer greater than zero. Otherwise, it
  just provides a short-hand way for people and the LSC to talk about
  Instances.

  Some of the other columns are calculated based on this identifier,
  but it is not a strict requirement.

Student Name
  This is the name of the student who will be using this instance. It
  is here to make it easier to associate an instance with the person
  who will be using it.

Mojang Accounts
  This is a list of one or more Mojang account names that will be
  included on the instance's whitelist. If multiple people should on
  the whitelist, separate names with commas. Whitespace is ignored.

  The special value of ``All Accounts`` indicates that the whitelist
  for this instance should be filled with all accounts listed for
  other instances. This makes it easy to construct a "Classroom Server"
  where any student with a private instance will also be included on
  the Classroom Server's whitelist.

  The special value of ``Open Server`` indicates that the whitelist
  for this instance should be left empty. In this case, Minecraft will
  permit anybody to connect.

  .. warning:: Beware that a truly open server can be joined by
               *anyone*. If you don't want this, you are recommended
               to use the whitelist.

Minecraft Port
  This is the TCP IP port at which the instance's Minecraft server
  will be available. Since the default Minecraft port is 25565, the
  default Control Sheet calculates port numbers based off the instance
  ID, using **565** as the suffix.

  Keep in mind that TCP restricts port numbers to integer values
  between 1 and 65,535. Ports between 1 and 1,024 are reserved for
  special purposes, so you should make sure the port numbers in this
  field fall between 1,025 and 65,535.

  .. note:: Since Minecraft defaults to port 25565 by default,
            students who forget to enter their assigned port number
            will try reach a server at this port. It is recommend that
            you run a specially configured server at this default
            port. This server could be open for all students to
            participate in (e.g., a Classroom Server), or it should be
            configured with no access, and a deny message that prompts
            students to enter their assigned port number.

IPython Port
  This is the TCP IP port at which the instance's IPython Notebook
  server will be available. Since the server runs over HTTPS, which
  uses port 443 by default, the default Control Sheet calculates port
  numbers based off the instance ID, using **443** as the suffix.

  Keep in mind that TCP restricts port numbers to integer values
  between 1 and 65,535. Ports between 1 and 1,024 are reserved for
  special purposes, so you should make sure the port numbers in this
  field fall between 1,025 and 65,535.

Student Password
  When a student connects to the IPython Notebook server with a web
  browser, it will prompt them to enter the password contained in this
  column. It is recommended that you generate the passwords in this
  list and then provide them to the students along with their assigned
  port numbers.

  The following command will generate a list of 30, 6-character
  passwords, each made up of lowercase letters and numbers, and
  excluding some characters that can be easily mistaken for each
  other::

    apg -a 1 -n 30 -m 6 -x 6 -M ln -E lI10OS

Instance Type
  The LSC knows how to deploy the instance types listed in the table
  below. Use the types listed below in the Control Sheet.

  +---------------+--------------------------------------------------+
  | Instance Type | Description                                      |
  +===============+==================================================+
  | STUDENT       | A normal student instance. Most of the           |
  |               | documentation in this file refers to this        |
  |               | Instance Type.                                   |
  +---------------+--------------------------------------------------+
  | REDIRECT      | An instance that denies all access with the      |
  |               | following message "You need to specify your      |
  |               | assigned Minecraft port. Please try again."      |
  +---------------+--------------------------------------------------+

Command
  This is the way you control the instances. This column should
  contain one of the values from the first column in the table
  below. The LSC interprets the command you entered and moves the
  instance into the desired state when the :command:`lsc
  process-commands` command is run.

  +----------------+----------------------------------------------------------+
  | Command        | Description                                              |
  +================+==========================================================+
  | RUN            | The instance should be moved to a normal, running state. |
  |                | This is the state where students can use the instance.   |
  +----------------+----------------------------------------------------------+
  | DOWN           | The instance should be stopped (if running), but the     |
  |                | files will be preserved.                                 |
  +----------------+----------------------------------------------------------+
  | RESETWORLD     | Stop the instance (if running) and clear out the world   |
  |                | files. This is most useful if the student has            |
  |                | done something horrible to their world and needs a fresh |
  |                | one to start over.                                       |
  +----------------+----------------------------------------------------------+
  | RESETNOTEBOOKS | Stop the instance (if running) and clear out the IPython |
  |                | notebook files. This is for when the student has         |
  |                | done something horrible to their notebook files and      |
  |                | and needs a fresh set to start over.                     |
  +----------------+----------------------------------------------------------+
  | DESTROY        | The instance should be stopped (if running) and all      |
  |                | related files are permanently erased.                    |
  +----------------+----------------------------------------------------------+

Status As Of
  Timestamp of when the Current Instance State was last updated. This
  should be pretty close to the current time. You should not manually
  edit this value.

Container IDs
  Hexadecimal identifiers of the container(s) that make up this
  instance. If there are multiple values, they will be separated by
  commas. You should not manually edit this value.

LSC Message
  This column will hold any instance-specific message from the LSC
  command. You should not manually edit this value.

S3 Bucket
  This is the address that will be used by the LOAD and SAVE
  commands. More to come as we flesh out this feature.

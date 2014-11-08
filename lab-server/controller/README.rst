================================================================
 CoderDojo Twin Cities, Python-Minecraft, Lab Server Controller
================================================================

The Lab Server Controller is a command line tool that helps manage the
lab server used for teaching the CoderDojo TC's Python-Minecraft code
group.

In summary, the Lab Server hosts a bunch of Instances. Each student
will get their own Instance. Each Instance hosts a private Minecraft
server, the RaspberryJuice plugin that lets Python talk to Minecraft,
and an IPython Notebook server that can talk to the Minecraft
server. These Instances give each student an isolated environment in
which they can work through lessons and challenges.

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
=============

Before you can use the LSC command for the first time, create a file
in your current directory named :file:`lsc.ini`. Populate it with
content like the following:

.. code-block:: ini

   [Lab Config Data]
   spreadsheet = Lab Server Controller
   worksheet = 2014-11-15
   email = youremail@example.com
   password = YOUR_APPLICATION_SPECIFIC_GOOGLE_PASSWORD

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
enter your main Google password in this field. Please consult the note
below for what to do instead.**

.. note:: Absolutely **everyone** ought to be using Google's `2-factor
authentication`_, especially people who need to write down their
password in a configuration file.  To make the LSC tool work when you
have it set up, you need to create an `application-specific
password`_.  The password you set up on that page should be the one
you enter in the config file.

.. _`2-factor authentication`: https://support.google.com/accounts/answer/180744?hl=en
.. _`application-specific password`: https://accounts.google.com/b/0/IssuedAuthSubTokens?hl=en&hide_authsub=1


Usage
=====

This section describes various usage examples. The name of the command
itself is :command:`lsc`. Each of the different subcommands follows
``lsc`` on the command line.


Environment Shakeout Commands
-----------------------------

The commands in this section help with environment shakeout.

The :command:`lsc test` command checks the environment. It confirms
that the config file is present. It validates that the information in
the config file allows it to reach the Control Sheet used to manage
the student instances.


Control Sheet Commands
----------------------

The commands in this section help with managing the Control Sheet.

The :command:`lsc show` command dumps the information from the Control
Sheet.

The :command:`lsc update-states` command walks through the Control
Sheet and attempts to move it from its current state to the desired
state, as indicated in the sheet.


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

Student's Name
  This is the name of the student who will be using this instance. It
  is here to make it easier to associate an instance with the person
  who will be using it.

Mojang Accounts
  This is a list of one or more Mojang account names that will be
  included on the instance's whitelist. If multiple people should on
  the whitelist, separate names with commas. Whitespace is ignored.

  The special value of ``All Accounts`` indicates that the whitelist
  for this instance should be filled with all accounts listed for
  other instances. This makes it easy to contruct a "Classroom Server"
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

IPython Password
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
  +---------------+--------------------------------------------------+
  | STUDENT       | A normal student instance. Most of the           |
  |               | documentation in this file refers to this        |
  |               | Instance Type.                                   |
  +===============+==================================================+
  | REDIRECT      | An instance that denys all access with the       |
  |               | following message "You need to specify your      |
  |               | assigned Minecraft port. Please try again."      |
  +---------------+--------------------------------------------------+

World Seed
  This is the Seed value used to create the Minecraft world within the
  Instance. Left blank, Minecraft will pick a seed at random, so each
  student will start off in a world unlike any other. Some seeds give
  a better starting point for some exercises, so it is recommended to
  find a good seed value and assign it to all students.

Desired Instance State
  This is the way you control the instances. This column should
  contain one of the values from the first column in the table
  below. The LSC uses this value to decide what to do with each
  instance when you the :command:`lsc update-states` command is run.

  +-----------+-------------------------------------------------------------+
  | Desired   |                                                             |
  | Instance  |                                                             |
  | State     | Description                                                 |
  +-----------+-------------------------------------------------------------+
  | UP        | The instance should be created (if necessary) and started.  |
  +===========+=============================================================+
  | DOWN      | The instance should be stopped (if running).                |
  +===========+=============================================================+
  | NONE      | Pretend like this row isn't present. This means "ignore me".|
  +===========+=============================================================+
  | DESTROY   | The instance should be stopped (if running) and destroyed   |
  |           | if present.                                                 |
  +===========+=============================================================+
  | RESTART   | The instance should be stopped and then restarted,          |
  |           | preserving the Minecraft world and any Python files the     |
  |           | student might have changed. This is like a reboot of the    |
  |           | instance.                                                   |
  +===========+=============================================================+
  | SAVE      | This pauses the instance and saves the current world and    |
  |           | the student's Python files into the S3 bucket.              |
  +===========+=============================================================+
  | LOAD      | This replaces the files inside the instance with those in   |
  |           | the student's S3 bucket.                                    |
  +-----------+-------------------------------------------------------------+

Current Instance State
  This column is updated when the :command:`lsc update-states` command
  is run. It is the way the LSC tells you what's going on with the
  instance. It will contain one of the values from the table
  below. You should not manually edit this value.

  +-----------+-------------------------------------------------------------+
  | Current   |                                                             |
  | Instance  |                                                             |
  | State     | Description                                                 |
  +-----------+-------------------------------------------------------------+
  | BAD INPUT | There is a problem interpreting the values on this          |
  |           | instance's row in the Control Sheet. Please check them.     |
  +===========+=============================================================+
  | UP        | The instance is up and running.                             |
  +-----------+-------------------------------------------------------------+

State As Of
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

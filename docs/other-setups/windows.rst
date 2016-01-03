.. _setup-windows:

=============================
 Setup for Microsoft Windows
=============================

These are the steps to get a full development environment working on a
Windows PC, in roughly the order you should perform them.


.. _system type:

Figure Out Your System Type
===========================

Some of the software installed below requires the correct choice to be
made between a 32-bit or 64-bit version of the software. You can learn
the proper choice for your computer by checking your Computer
Properties:

 #. From your desktop, choose :menuselection:`Start`, then right-click
    on :menuselection:`Computer` and choose
    :menuselection:`Properties`.

 #. In the window that opens, look for the :guilabel:`System type`
    under :guilabel:`System`. On a 64-bit system, it will say ``64-bit
    Operating System``.

    .. note:: Remember this value for later.


Working Directory
=================

Much of the work we do will involve a set of files on your
computer. It's helpful if you organize these into a single
location. On a Windows PC, the default place for user files is in the
:file:`Documents` folder. We will start from there:

 #. From your desktop, choose :menuselection:`Start --> Documents` to
    open a Windows Explorer view of your :file:`Documents` folder.

 #. In the window that opens, right-click in the main window and
    choose :menuselection:`New --> Folder`. Give it the name
    :file:`CoderDojo`.

 #. Double-click into the :file:`CoderDojo` folder and again,
    right-click in the main window and choose :menuselection:`New -->
    Folder`. Give this one the name :file:`MinecraftMod`.

    .. note:: From here on, we will refer to this as your
	      :file:`MinecraftMod` folder.

 #. Double-click into the :file:`MinecraftMod` folder and again,
    right-click in the main window and choose :menuselection:`New -->
    Folder`. Give this one the name :file:`CanaryMod`.


TortoiseGit and Git for Windows
===============================

TortoiseGit is a nice, GUI wrapper for Git on Windows. With this, you
can use Git entirely from within Windows Explorer.

 #. Visit the `TortoiseGit download page
    <https://code.google.com/p/tortoisegit/wiki/Download>`_. Select
    the appropriate version based on your `system type`_ and download
    it.

 #. Once the file has downloaded, run it. You can leave all the
    installer options at their defaults. Allow it to install.

 #. Visit the `git for windows download page
    <http://msysgit.github.io>`_. Click on the :guilabel:`Download`
    link.

 #. Once the file has downloaded, run it. You can leave all the
    installer options at their defaults. Allow it to install.

 #. Now is a good time to reboot your PC.


CanaryMod Server
================

 #. Visit the `CanaryMod download page
    <http://canarymod.net/releases/canarymod-1710-112>`_.

 #. Right click on the link to the Jar file and save it within the
    :file:`MinecraftMod\\CanaryMod` folder.

 #. In the :file:`MinecraftMod\\CanaryMod` folder, create a new file
    named :file:`startserver.bat`, and give it the following
    contents::

      CanaryMod-1.7.10-1.1.2.jar
      pause

 #. In the :file:`MinecraftMod\\CanaryMod` folder, create a new file
    named :file:`eula.txt`, and give it the following contents::

      eula=true

Give the CanaryMod server a test run by double-clicking on the
:command:`startserver.bat` script you created. The
:guilabel:`CanaryMod: Minecraft server` window should open, and you
should see log messages indicating that the server is running.


RaspberryJuice for CanaryMod
============================

We're going to use Git to clone the repository where RaspberryJuice
comes from. The Jar file containing the plugin is available in the
repository, so we will copy it from there.

 #. Visit the GitHub page for the `CanaryRaspberryJuice plugin
    <https://github.com/martinohanlon/CanaryRaspberryJuice>`_.

 #. On the right-hand side of the page, you will see a field labeled
    :guilabel:`HTTPS clone URL`. Copy the value from here into your
    clipboard. It will be something like
    ``https://github.com/martinohanlon/CanaryRaspberryJuice.git``.

 #. Using Windows Explorer, navigate to your :file:`MinecraftMod`
    folder.

 #. Right-click within the main panel and choose :menuselection:`Git
    Clone...`.

 #. In the window that opens, double check that the :guilabel:`URL`
    field contains the one you copied above, that the
    :guilabel:`Directory` field specifies the
    :file:`MinecraftMod\\CanaryRaspberryJuice` folder, and then click
    :guilabel:`OK`.

 #. After the Clone process finishes, open the
    :file:`MinecraftMod\\CanaryRaspberryJuice\\jars` folder. Copy the
    file named :file:`canaryraspberryjuice-1.0.jar` into
    :file:`MinecraftMod\\CanaryMod\\plugins`.

Restart the CanaryMod server again (double-clicking on the
:command:`startserver.bat` script). This time, among the log messages,
you should see one that reads ``[INFO]: Enabling
CanaryRaspberryJuicePlugin Version 1.0``.


Minecraft
=========

 #. Visit the `Minecraft download page
    <https://minecraft.net/download>`_.

 #. Right click on the :file:`Minecraft.exe` and save it into your
    :file:`MinecraftMod` folder.

 #. Do the same with the :file:`Minecraft_server.1.8.9.exe` file. We
    plan to use the CanaryMod server instead, but it may be useful to
    have the vanilla server for troubleshooting.

 #. Give Minecraft a test run by opening the :file:`MinecraftMod`
    folder in Windows Explorer. Then double-click on
    :file:`Minecraft.exe`.

 #. Once the Minecraft Launcher opens, create a new Profile that is
    configured to use Minecraft version 1.7.10 (consistent with the
    CanaryMod server version).

    #. Click :guilabel:`New Profile`.

    #. In the :guilabel:`Profile Editor` dialog, change the fields as
       follows:

       +--------------------------+-------------------------+
       | Field                    | Value                   |
       +==========================+=========================+
       | :guilabel:`Profile Name` | ``MinecraftMod 1.7.10`` |
       +--------------------------+-------------------------+
       | :guilabel:`Use version`  | ``release 1.7.10``      |
       +--------------------------+-------------------------+

       Then click :guilabel:`Save Profile`.


Python 2.7.8 for Windows
========================

 #. Visit the `Python Downloads page for Windows
    <https://www.python.org/downloads/windows/>`_.

 #. Be sure to locate the **2.7.8** version of Python, and then select
    the right installer based on your `system type`_.

 #. Once the file has downloaded, run it. You can leave all the
    installer options at their defaults. Allow it to install.


CoderDojo TC's ``python-minecraft`` Repository
==============================================

We're going to use Git to clone the repository where the CoderDojo
Twin Cities chapter has stored the example Python scripts.

 #. Visit the GitHub page for the `CoderDojoTC python-minecraft
    repository <https://github.com/CoderDojoTC/python-minecraft>`_.

 #. On the right-hand side of the page, you will see a field labeled
    :guilabel:`HTTPS clone URL`. Copy the value from here into your
    clipboard. It will be something like
    ``https://github.com/CoderDojoTC/python-minecraft.git``.

 #. Using Windows Explorer, navigate to your :file:`MinecraftMod`
    folder.

 #. Right-click within the main panel and choose :menuselection:`Git
    Clone...`.

 #. In the window that opens, double check that the :guilabel:`URL`
    field contains the one you copied above, that the
    :guilabel:`Directory` field specifies the
    :file:`MinecraftMod\\python-minecraft` folder, and then click
    :guilabel:`OK`.


Environment Shakeout
====================

Now that all the necessary parts have been installed, let's see if
everything is in working order.

 #. Shut down the Minecraft game, if it is running. Shut down the
    CanaryMod server, if it is running.

 #. Start the CanaryMod server by double-clicking on the
    :command:`startserver.bat` script you created in the
    :file:`MinecraftMod\\CanaryMod` folder.

 #. Start Minecraft by opening the :file:`MinecraftMod` folder in
    Windows Explorer. Then double-click on :file:`Minecraft.exe`.

 #. Once the Minecraft Launcher opens, choose the ``MinecraftMod
    1.7.10`` Profile, and click :guilabel:`Play`.

 #. Once the game starts, click the :guilabel:`Multiplayer`
    button. Choose the :guilabel:`Direct Connect` button on the next
    page. Enter ``localhost`` in the :guilabel:`Server Address` button
    and then press :guilabel:`Join Server`.

 #. Once your player has joined the game, from the Windows desktop,
    choose :menuselection:`Start --> All Programs --> Python 2.7 -->
    IDLE (Python GUI)` to open a Python Shell.

 #. In the Python Shell, choose :menuselection:`File --> Open...` and
    navigate to the :file:`MinecraftMod\\python-minecraft`
    folder. Choose :file:`hello_world.py`.

 #. Choose :menuselection:`Run --> Run Module`, and look for the
    "Hello Minecraft" message within the game.

If you saw the "Hello Minecraft" message, congratulations! You are
ready to proceed. If you ran into any problems with the environment
shakeout, you should examine the error messages you might be seeing,
think about what they might mean, and revisit the appropriate section
of this document. Or, ask for help!

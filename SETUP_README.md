How do I run these things?
--------------------------

If you're going to be at a CoderDojoTC event in the near future, we can get your environment up and running for you.

If you will not be attending CoderDojoTC or you want to get your environment sorted out ahead of time, here is a general guide for getting things set up:

####Set up the CraftBukkit server
<ol><li>Follow <a href="http://blog.lostbearlabs.com/2013/04/25/using-the-minecraft-api-without-a-raspberry-pi-craftbukkit-and-raspberryjuice/" target="_blank">these instructions</a> for setting up an environment without a Raspberry PI.
<ul><li>They will direct you <a href="http://wiki.bukkit.org/Setting_up_a_server" target="_blank">here</a> to set up the server.</li><li>Make sure you download the 1.6.4 jar file, as the api and scripts included in this repository are compatible with the 1.6.4 client and server.</li></ul></li><li>If you download the latest client (launcher), you'll need to set the version back to 1.6.4 by clicking on <b>Edit Profile</b> and selecting <b>release 1.6.4</b> from the <b>Use version</b> drop-down.</li><li>Once you have the server up and running, you can download any number of fun plugins <a href="http://dev.bukkit.org/bukkit-plugins/" target="_blank">here</a>. To install a plugin, download the jar file, move it to the server's plugins folder, and restart the server.<ul><li>We highly recommend installing the <a href="http://dev.bukkit.org/bukkit-plugins/always-day/files/15-always-day-v2-2-8/" target="_blank">AlwaysDay</a> plugin</li></ul></li></ol>

####Python editor
In the CoderDojoTC sessions, we use [IDLE](https://docs.python.org/2/library/idle.html) to run the Python scripts.

IDLE comes bundled with Python. If your machine does not already have IDLE, download Python 2.7 for your machine [here](https://www.python.org/download/releases/2.7.7/).

####Running the scripts
1. If you haven't done so already, start the CraftBukkit server by double clicking on the *start.command* file. A Terminal or DOS window will open and you'll see server log text accumulate here. When the server is done loading, you will see something like this: `[INFO] Done (1.599s)! For help, type "help" or "?"` If there are errors in the server log, make sure you are connected to the internet and make sure you have installed Java as part of the server setup instructions above. These are the two most common errors we see during server startup.
2. Launch the Minecraft client if you haven't already, login, click Play, and join your server (localhost:25565). (If you do not already have a Minecraft login, you can get one <a href="https://account.mojang.com/register" target="_blank">here</a>.)
3. Open the script you'd like to run in IDLE or another text editor or development environment.
4. Make any modifications you'd like to make to the script.
5. Save the script.
6. If you're using IDLE, hit *F5* or select *Run Module* from the *Run* menu. Otherwise, you can run the script from the command line (Terminal or DOS) by changing to the directory the script is contained in and typing `python` followed by the name of the script you'd like to run.
7. While the script is running, you should see more server logs accumulate in the server Terminal or DOS window.
8. When the script completes, return to your Minecraft world to see the results.

####Tips and tricks
* If you accidentally create a 1-million-block-radius solid sphere of TNT and your server freezes, you may at any time abandon the world you have created and start over by stopping the server, deleting the *world* and *world_the_end* directories, and restarting the server.
* You may type in any [Minecraft Commands](http://minecraft.gamepedia.com/Commands) directly at the server prompt in the Terminal or DOS window where your server is running.

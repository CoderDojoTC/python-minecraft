python-minecraft
================

Example Python scripts for use with Minecraft at CoderDojo Twin Cities.

The actual MCPi API v0.1_1 has been unceremoniously included in this repository in the interest of getting students up and running quickly. It was obtained from [pi.minecraft.net](http://pi.minecraft.net/).

Go [here](/SETUP_README.md) for instructions on how to get your environemnt up and running.

Coordinate System
------------------
Most coordinates are in the form of a three integer vector (x,y,z) which address a specific tile in the game world. (0,0,0) is the spawn point sea level. (x,z) is the ground plane and Y is towards the sky. In other words, x is left and right, z is forward and backward, and y is up and down.

![Minecraft's odd x-y-z coordinate system](/ignoreme/coordinates.png)

Minecraft Programming Reference
--------------------------------

These are just a few highlights. A more detailed reference can be found [here](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)

###World

####`world.getBlock(x, y, z)`
Look up the type of block at the specified coordinates.

####`world.setBlock(x, y, z, block_type)`
Set the block at the specified coordinates to the type block_type.

####`world.setBlocks(x1, y1, z1, x2, y2, z2, block_type)`
Create a set of blocks starting at one coordinate point extending to another point with blocks of the type block_type. This can be used to make cubes or rectangles.

####`world.getHeight(x, z)`
Look up the height (y coordinate) of the tallest brick at the specified x and y coordinates.

####`world.postToChat(“Message”)`
Send a message over chat.

###Player

####`player.getPos()`
Look up the coordinates that the player is currently positioned at.

####`player.setPos(x,y,z)`
Set the player’s position to the specified coordinates.

###Blocks
[mcpi/block.py](https://github.com/sarahhagstrom/python-minecraft/blob/master/mcpi/block.py) is the ultimate authority on which blocks are available for your use. Those code constants are copied and pasted here for convenience. The underlying engine actually provides all of [these](http://minecraft.gamepedia.com/Data_values_(Pocket_Edition)) blocks, not all of which are included in the MCPi block module. You are free to edit mcpi/block.py to add more blocks using the decimal value listed and following the pattern you find in [block.py](https://github.com/sarahhagstrom/python-minecraft/blob/master/mcpi/block.py).

    AIR
    STONE
    GRASS
    DIRT
    COBBLESTONE
    WOOD_PLANKS
    SAPLING
    BEDROCK
    WATER_FLOWING
    WATER
    WATER_STATIONARY
    LAVA_FLOWING
    LAVA
    LAVA_STATIONARY
    SAND
    GRAVEL
    GOLD_ORE
    IRON_ORE
    COAL_ORE
    WOOD
    LEAVES
    GLASS
    LAPIS_LAZULI_ORE
    LAPIS_LAZULI_BLOCK
    SANDSTONE
    BED
    COBWEB
    GRASS_TALL
    WOOL
    FLOWER_YELLOW
    FLOWER_CYAN
    MUSHROOM_BROWN
    MUSHROOM_RED
    GOLD_BLOCK
    IRON_BLOCK
    STONE_SLAB_DOUBLE
    STONE_SLAB
    BRICK_BLOCK
    TNT
    BOOKSHELF
    MOSS_STONE
    OBSIDIAN
    TORCH
    FIRE
    STAIRS_WOOD
    CHEST
    DIAMOND_ORE
    DIAMOND_BLOCK
    CRAFTING_TABLE
    FARMLAND
    FURNACE_INACTIVE
    FURNACE_ACTIVE
    DOOR_WOOD
    LADDER
    RAIL
    STAIRS_COBBLESTONE
    DOOR_IRON
    REDSTONE_ORE
    SNOW
    ICE
    SNOW_BLOCK
    CACTUS
    CLAY
    SUGAR_CANE
    FENCE
    GLOWSTONE_BLOCK
    BEDROCK_INVISIBLE
    STONE_BRICK
    GLASS_PANE
    MELON
    FENCE_GATE
    GLOWING_OBSIDIAN
    NETHER_REACTOR_CORE

Minecraft Controls
------------------

###Keyboard
<table><tbody>
<tr><td>W,A,S,D</td><td>Move (navigate inventory)</td></tr>
<tr><td>SPACE</td><td>Jump, double tap to start/stop flying, hold to fly higher</td></tr>
<tr><td>SHIFT</td><td>Sneak, hold to fly lower</td></tr>
<tr><td>E</td><td>Open inventory</td></tr>
<tr><td>18</td><td>Select inventory slot item to us</td></tr>
<tr><td>ESC</td><td>Show/hide menu</td></tr>
<tr><td>TAB</td><td>Release mouse without showing menu</td></tr>
<tr><td>ENTER</td><td>Confirm menu selection</td></tr>
</tbody></table>

###Mouse
<table><tbody>
<tr><td>Steer</td><td>Look/turn around</td></tr>
<tr><td>Left button</td><td>Remove block (hold)</td></tr>
<tr><td>Right button</td><td>Place block, hit block with sword</td></tr>
<tr><td>Mouse wheel</td><td>Select inventory slot item to use</td></tr>
</tbody></table>

Resources and Credits
----------------------

###Online Coding Classes
[Codecademy](http://www.codecademy.com/)<br>
[LearnPython.org](http://www.learnpython.org/)<br>
[Udacity](https://www.udacity.com/)<br>

###More about the Minecraft API
[MCPi API Basics](http://www.stuffaboutcode.com/2013/01/raspberry-pi-minecraft-api-basics.html)<br>
[MCPi API Tutorial on StuffAboutCode.com](http://www.stuffaboutcode.com/2013/04/minecraft-pi-edition-api-tutorial.html)<br>
[MCPi API Reference](http://www.stuffaboutcode.com/p/minecraft-api-reference.html)<br>
[MCPi API Examples](http://www.stuffaboutcode.com/2013/02/raspberry-pi-minecraft-install.html)<br>
[More MCPi scripts](https://github.com/brooksc/mcpipy)<br>

Note that although the StuffAboutCode links discuss using an Raspberry Pi, you don't need a Raspberry Pi to use the API. We're using CraftBukkit's local server instead. More information about that is [here](/SETUP_README.md)


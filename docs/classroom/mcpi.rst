===================================
 Controlling Minecraft from Python
===================================

Coordinate System
=================

Most coordinates are in the form of a three integer vector (x,y,z)
which address a specific tile in the game world. (0,0,0) is the spawn
point sea level. (X,Z) is the ground plane, and Y is towards the
sky. In other words, X is left and right, Z is forward and backward,
and Y is up and down.

.. figure:: _images/coordinates.png

   Minecraft's odd x-y-z coordinate system


Minecraft Programming Reference
===============================

These are just a few highlights. A more detailed reference can be
found in the `full API reference`_.

.. _full API reference: http://www.stuffaboutcode.com/p/minecraft-api-reference.html


World
-----

.. py:function:: world.getBlock(x, y, z)

   Look up the type of block at the specified coordinates.

.. py:function:: world.setBlock(x, y, z, block_type)

   Set the block at the specified coordinates to the type block_type.

.. py:function:: world.setBlocks(x1, y1, z1, x2, y2, z2, block_type)

   Create a set of blocks starting at one coordinate point extending
   to another point with blocks of the type block_type. This can be
   used to make cubes or rectangles.

.. py:function:: world.getHeight(x, z)

   Look up the height (y coordinate) of the tallest brick at the
   specified x and y coordinates.

.. py:function:: world.postToChat("Message")

   Send a message over chat.


Player
------

.. py:function:: player.getPos()

   Look up the coordinates that the player is currently positioned at.

.. py:function:: player.setPos(x,y,z)

   Set the player’s position to the specified coordinates.


Blocks
------

As is the case in most things related to programming, the
:file:`mcpi/block.py` `source code file`_ is the ultimate authority
for which blocks are available for your use. The table below lists
those constants and includes a few notes about some of the blocks.

.. _source code file: https://github.com/CoderDojoTC/python-minecraft/blob/master/mcpi/block.py

=======================  ===================================================
Block Name               Notes
=======================  ===================================================
``AIR``
``STONE``
``GRASS``
``DIRT``
``COBBLESTONE``
``WOOD_PLANKS``          Use ``block_data`` to control what kind of planks.
``SAPLING``
``BEDROCK``
``WATER_FLOWING``
``WATER``                An alias for ``WATER_FLOWING``
``WATER_STATIONARY``
``LAVA_FLOWING``
``LAVA``                 An alias for ``LAVA_FLOWING``
``LAVA_STATIONARY``
``SAND``
``GRAVEL``
``GOLD_ORE``
``IRON_ORE``
``COAL_ORE``
``WOOD``                 Use ``block_data`` to control what kind of wood.
``LEAVES``
``GLASS``
``LAPIS_LAZULI_ORE``
``LAPIS_LAZULI_BLOCK``
``SANDSTONE``
``BED``
``COBWEB``
``GRASS_TALL``
``WOOL``                 Use ``block_data`` to control what color wool.
``FLOWER_YELLOW``
``FLOWER_CYAN``
``MUSHROOM_BROWN``
``MUSHROOM_RED``
``GOLD_BLOCK``
``IRON_BLOCK``
``STONE_SLAB_DOUBLE``
``STONE_SLAB``
``BRICK_BLOCK``
``TNT``
``BOOKSHELF``
``MOSS_STONE``
``OBSIDIAN``
``TORCH``
``FIRE``
``STAIRS_WOOD``
``CHEST``
``DIAMOND_ORE``
``DIAMOND_BLOCK``
``CRAFTING_TABLE``
``FARMLAND``
``FURNACE_INACTIVE``
``FURNACE_ACTIVE``
``DOOR_WOOD``
``LADDER``
``RAIL``
``STAIRS_COBBLESTONE``
``DOOR_IRON``
``REDSTONE_ORE``
``SNOW``
``ICE``
``SNOW_BLOCK``
``CACTUS``
``CLAY``
``SUGAR_CANE``
``FENCE``
``GLOWSTONE_BLOCK``
``BEDROCK_INVISIBLE``
``STONE_BRICK``
``GLASS_PANE``
``MELON``
``FENCE_GATE``
``GLOWING_OBSIDIAN``
``NETHER_REACTOR_CORE``
=======================  ===================================================

The underlying engine actually provides all of `these block types`_.
If you see one is missing from the MCPI ``block`` module, you are free
to edit :file:`mcpi/block.py` to add more blocks using the decimal
value listed and following the pattern you find in the existing code.

.. _these block types: http://minecraft.gamepedia.com/Data_values_(Pocket_Edition)

#! /usr/bin/python
import sys
sys.path.append( "~/Desktop/CoderDojo")
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z] =  world.player.getPos()
#[x,y,z] =  [-1011,4,-930]

# Set some variables to customize your pyramid
height    =  25
material  =  block.STONE_SLAB

# This variable will track the current level being created inside the loop
level  =  1

# Execute the loop, building from the top down
while level <= height:
	print level
	world.setBlocks( x - level, height - level, z - level, x - level, height - level, z + level, material )
	world.setBlocks( x - level, height - level, z - level, x + level, height - level, z - level, material )
	world.setBlocks( x - level, height - level, z + level, x + level, height - level, z + level, material )
	world.setBlocks( x + level, height - level, z - level, x + level, height - level, z + level, material )
	level  =  level + 1;

# Put the player on top of the pyramid!
world.player.setPos( x, height, z )

#!/usr/bin/python
import sys
sys.path.append( "~/Desktop/CoderDojo")
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z] =  world.player.getPos()

# Set some variables to customize your tower
width     =  10
height    =  10 
material  =  block.SANDSTONE

# Execute the loop, building from the bottom up
for column in range( 0, width ):
	for level in range( 0, height ):
		world.setBlock( x+column, level, z, material )

# Put the player on top of the tower
world.player.setPos( x, height, z )

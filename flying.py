#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

# Get the player's current position and store the coordinates
[x,y,z]  =  world.player.getPos()

# Look up the block material for the coordinate directly underneath the player
blockId  =  world.getBlock( x, ceil( y ) - 1, z )

# If the player's y coordinate position is greater than 0, then they must be 
# flying or walking on stilts!  AIR has block ID 0 so if that's what is under
# the player, they must be flying.
flying  =  blockId == 0

if flying:
	print "You are flying high!"
else:
	print "You are on the ground."


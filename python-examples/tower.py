#!/usr/bin/python
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()  
# Get the player's current position and store the coordinates
[x,y,z] =  world.player.getPos()

# Set some variables to customize your tower
height    =  10
material  =  block.TNT
length = 

level  =  0
keep_building  =  True

for n in range (0,length):
  for p in range(0,height):
    world.setBlock( x+n, y+p, z, material )


# Put the player on top of the tower
world.player.setPos( x, height, z )

#!/usr/bin/python
import sys
sys.path.append( "~/Desktop/CoderDojo")
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()
[x0,y0,z0] = world.player.getPos()
y0=y0+60
#y0=y0+r+r

r=20
material = block.GLOWING_OBSIDIAN
for x in range(-r,r):
  for y in range(-r,r):
    for z in range(-r,r):
      if x**2 + y**2 + z**2 < r**2:
        if y % 2 == 0:
          world.setBlock( x0+x, y0+y, z0+z, material );


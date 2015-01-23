#!/usr/bin/python
import sys
sys.path.append( "~/Desktop/CoderDojo")
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()
# Get Steve's current position
[x0,y0,z0] = world.player.getPos()

# Set the radius of the sphere
r=20
material = block.WOOD

# Put the bottom edge of the sphere 8 blocks above Steve's head
y0=y0+r+8

for x in range(-r,r):
  for y in range(-r,r):
    for z in range(-r,r):
	  # If we were making a cube, we'd put a block here
      candidate_location = x**2 + y**2 + z**2
	  # But we're not, so if this falls outside of the sphere or wholly inside of it, skip this iteration
      if candidate_location < r**2 and candidate_location > (r-1)**2:
		# This location qualifies, so put a block here
        world.setBlock(x0+x, y0+y, z0+z, material);

print "Hollow sphere built successfully! Return to the game and look above you."

# Things to try:
# How could we make this a solid sphere?
# How could we nest a smaller sphere inside a larger one?
# How could we nest a hollow sphere inside a solid block? (How about an AIR sphere inside a WOOD block?)
# How could we make it a half sphere?
# How could we make it so the sphere is separated into 2 halves?
# How could we make the border into ribbons instead of a solid wall?
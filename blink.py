#!/usr/bin/python
# Written by Eric Johnson for CoderDojo Twin Cities - www.coderdojotc.org
# Creates a block, near the player's initial position, that changes material each second
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to the Minecraft server
world = minecraft.Minecraft.create()

print "THIS SCRIPT WILL RUN FOREVER IF YOU LET IT"
print "TYPE CTRL+C TO EXIT"

# Get the player's current position and store the coordinates
[x, y, z] = world.player.getPos()

materials = [block.GRASS, block.WOOL, block.BRICK_BLOCK]
n = 0
while True:
    n = (n + 1) % len(materials)
    material = materials[n]
    world.setBlock(x+1, y, z+1, material)
    time.sleep(1)

#!/usr/bin/python
# Written by Eric Johnson for CoderDojo Twin Cities - www.coderdojotc.org
# Creates a rain of blocks around the player's current position
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# Connect to the Minecraft server
world = minecraft.Minecraft.create()

print "THIS SCRIPT WILL RUN FOREVER IF YOU LET IT"
print "TYPE CTRL+C TO EXIT"

material = block.ICE  # we like sand because it is subject to gravity -- create it up high, and it will fall
while True:
    # Get the player's current position and store the coordinates
    [x, y, z] = world.player.getPos()
    dx = random.randint(-10, 10)  # somewhere nearby
    dz = random.randint(-10, 10)  # somewhere nearby
    dy = random.randint(5, 15)  # somewhere above!
    world.setBlock(x+dx, y+dy, z+dz, material)
    time.sleep(0.5)

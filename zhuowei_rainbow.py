#!/usr/bin/env python

#
# mcpipy.com retrieved from URL below, written by zhuowei
# http://www.minecraftforum.net/topic/1638036-my-first-script-for-minecraft-pi-api-a-rainbow/

import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import server

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create(server.address)
height = 64

mc.player.setPos( 0, height, height )

mc.setBlocks(-(height*2),0,0,(height*2),height + len(colors),0,0)
for x in range(0, 128):
        for colourindex in range(0, len(colors)):
                y = sin((x / (height*2.0)) * pi) * height + colourindex
                mc.setBlock(x - (height*2), int(y), 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])

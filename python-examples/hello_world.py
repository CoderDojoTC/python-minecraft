#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

world.postToChat("Hello Minecraft!")

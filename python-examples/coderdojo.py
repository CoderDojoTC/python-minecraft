#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import minecraft_letters as letters

# Connect to the Minecraft server
world  =  minecraft.Minecraft.create()

letters.write( world, "Rock AND Roll", block.TNT );

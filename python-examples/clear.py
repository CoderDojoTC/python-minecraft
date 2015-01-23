#!/usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import sys

""" clearZone clears an area and sets a stone floor
    takes two x,z pairs clears everything above 0y and then sets
    a stone floor at -1y
    @author: goldfish

	Modified by Jessica Zehavi for CoderDojo Twin Cities
	http://www.coderdojotc.org 
"""

def clearZone( size ):
	mc.player.setPos(0,0,0)
	[x,y,z] = [0,0,0];
	mc.setBlocks( x - size, 0, z - size, x + size, size, z + size, block.AIR )
	mc.setBlocks( x - size , -1, z - size, x + size, -1, z + size, block.STONE )

if __name__ == "__main__":
	mc = minecraft.Minecraft.create( )

	try:
		size  =  sys.argv[1]
		mc.postToChat( "Clearing things up a bit..." )
		print "Clearing a", size, "x", size, "area around your position."
		clearZone( int(size) )
	except:
		print "Specify the size of zone you would like to clear."
		print "Syntax:", sys.argv[0], "<size in blocks>"



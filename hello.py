import mcpi.minecraft as minecraft
import mcpi.block as block

world = minecraft.Minecraft.create()

[x,y,z] = world.player.getPos()
world.postToChat( "Position is: %d %d %d" % (x,y,z) )

world.player.setPos( 0, 64, 0 )

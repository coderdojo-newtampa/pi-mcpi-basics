#
# Draw a cube
#
# Slightly above player
#

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
x=pos.x + 3
y=pos.y + 2
z=pos.z

mc.setBlocks(x,y,z, x+3,y+3,z+3, block.IRON_BLOCK.id)

#
# Draw a rectangle
#
# Slightly above player
#

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("192.168.1.5")

pos = mc.player.getPos()
x=pos.x + 3
y=pos.y + 2
z=pos.z

mc.setBlocks(x,y,z, x+6,y+3,z, block.MOSS_STONE.id)
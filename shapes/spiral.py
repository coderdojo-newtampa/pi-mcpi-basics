#
# Expanding square shapes
#
# Slightly above player
#

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("192.168.1.5")

def drawsquare(x,y,z,w):
    b = block.BRICK_BLOCK
    mc.setBlocks(x-w/2,y-w/2,z, x+w/2,y-w/2,z, b)
    mc.setBlocks(x-w/2,y+w/2,z, x+w/2,y+w/2,z, b)
    mc.setBlocks(x-w/2,y-w/2,z, x-w/2,y+w/2,z, b)
    mc.setBlocks(x+w/2,y-w/2,z, x+w/2,y+w/2,z, b)

pos = mc.player.getPos()
x=pos.x + 5
y=pos.y + 10
z=pos.z + 5

for w in range(2,20,4):
    drawsquare(x,y,z,w)

#
# Add flowers to the world!
#
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    pos=mc.player.getPos()
    mc.setBlock(pos.x,pos.y,pos.z, block.FLOWER_YELLOW.id)
    time.sleep(0.1)

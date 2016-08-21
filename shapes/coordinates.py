#
# Demonstrate 3D space (x,y,z)
#
# Will move x,y,z axes in the (-) and then (+) directions
#

import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create("192.168.1.5")

#mc.player.setPos(0,10,0)

mc.postToChat("Orange is X-Axis, Blue is Y-Axis, Purple is Z-Axis (x,y,z)")

for i in (-1,-2,-3,-4,-5,1,2,3,4,5):
    if (i>0):
        print("Moving in the (+) positive direction")
    else:
        print("Moving in the (-) negative direction")

    mc.setBlocks(-20,0,-20,20,20,20,block.AIR.id)
    mc.setBlocks(
               -10+i,5,0,
               10+i,5,0,
               block.WOOL.id,1)

    mc.setBlocks(
               0,5,-10+i,
               0,5,10+i,
               block.WOOL.id,2)

    mc.setBlocks(
              0,10+i,0,
              0, 0+i,0,
              block.WOOL.id,3)

    print(i)
    time.sleep(1)
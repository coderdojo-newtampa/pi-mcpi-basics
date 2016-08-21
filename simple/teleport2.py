#
# Teleports you to a "safe" location in the minecraft world
#
# Program randomly places the player in a location that is:
#
#   At the "top" (heightest) point of an (x,z) location (using mc.getHeight())
#   A location where the bottom block is not AIR or any type of WATER
#
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

done = False

while not done:
    x=random.randrange(-127,127)
    z=random.randrange(-127,127)
    y = mc.getHeight(x,z)

    block_beneath = mc.getBlock(x,y-1,z)

    mc.postToChat("Teleporting ...")
    if (block_beneath not in {block.AIR.id, block.WATER.id, block.WATER_STATIONARY.id, block.WATER_FLOWING.id}):
        mc.player.setPos(x,y,z)
        mc.postToChat("Teleported!")
        done = True

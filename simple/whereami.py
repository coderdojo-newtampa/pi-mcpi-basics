#
# Find your place in the world
#
# Location printed on minecraft console in x,y,z order
#
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create("192.168.1.5")
pos = mc.player.getPos()
mc.postToChat("You are at " + str(pos))
print(mc.getBlock(pos.x, pos.y-1, pos.z))

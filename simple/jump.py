#
# Jump!
#
# Simulate a jump by moving the character upwards using a loop affecting the player's y value
# Note we don't bother to move the character down, as gravity takes care of that
#
import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
height = 20

for y in range(height):
    pos.y += 1
    mc.player.setPos(pos)
    time.sleep(0.01)

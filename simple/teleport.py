#
# Randomly go anywhere in the world
#
# Note: This program can get you stuck between rocks, drop you in water, or in the air!
#
import mcpi.minecraft as minecraft
import random

mc = minecraft.Minecraft.create()

x=random.randrange(-127,127)
y=random.randrange(0,100)
z=random.randrange(-127,127)

mc.player.setPos(x,y,z)

#
# Hello world in the Minecraft window
#
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create("192.168.1.5")
mc.postToChat("Hello world!")
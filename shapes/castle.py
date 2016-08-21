#
# Builds a castle
#
# Build 2 walls, and 1 tower with:
#  * Battlements
#  * Some doors
#  * Stairs to get around
#  * Torches on first floor of tower
#
# Work in progress!
#

import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

kingdomwidth = 71
castlewidth  = 31

def builddoor(x,y,z,height):
    mc.setBlocks(x,y+1,z,x,y+height,z, block.AIR)

def buildstairs(x,y,z,length, dir=1):
    xx = x
    yy = y
    zz = z
    #length=1
    for h in range(0,length):
        #mc.setBlocks(xx, y, z, xx, yy, zz, block.AIR.id)
        mc.setBlocks(xx, y, z, xx, yy, zz, block.STONE_SLAB_DOUBLE.id,2)
        mc.setBlock(xx, yy, zz, block.STAIRS_WOOD.id)
        yy+=1
        xx+=dir

        mc.setBlocks(xx-1,yy,zz,xx-2,yy+1,zz, block.AIR.id)

def buildwall(x,y,z,w,h,dir,battlements = False, battlement_walkway = False):
    w = round(w)

    yy = y + h - 1
    if  (dir == "n"):
        x0=x-w; x1=x+w
        z0=z+w; z1=z+w
        if (battlement_walkway):
            mc.setBlocks(x0+1, yy, z0-1, x1-1, yy, z1-2, block.STONE_SLAB.id,2)
            mc.setBlocks(x0+1, yy-1, z0-1, x1-1, yy-1, z1-2, block.STONE_BRICK.id)
    elif (dir == "s"):
        x0=x-w; x1=x+w
        z0=z-w; z1=z-w
        if (battlement_walkway):
            mc.setBlocks(x0+1, yy, z0+1, x1-1, yy, z1+2, block.STONE_SLAB.id,2)
            mc.setBlocks(x0+1, yy-1, z0+1, x1-1, yy-1, z1+2, block.STONE_BRICK.id)
    elif (dir == "e"):
        x0=x-w; x1=x-w
        z0=z-w; z1=z+w
        if (battlement_walkway) :
            mc.setBlocks(x0+1, yy, z0+1, x1+2, yy, z1-1, block.STONE_SLAB.id,2)
            mc.setBlocks(x0+1, yy-1, z0+1, x1+2, yy-1, z1-1, block.STONE_BRICK.id)
    else:
        x0=x+w; x1=x+w
        z0=z-w; z1=z+w
        if (battlement_walkway):
            mc.setBlocks(x0-1, yy, z0+1, x1-2, yy, z1-1, block.STONE_SLAB.id,2)
            mc.setBlocks(x0-1, yy-1,z0+1,x1-2, yy-1, z1-1, block.STONE_BRICK.id)

    mc.setBlocks(x0,y,z0,x1,y+h,z1, block.STONE_BRICK.id)

    if (battlements):

        if (dir in {"n", "s"}):
            for xx in range((int)(x0)+1, (int)(x1),2):
                if (dir == "n"):
                    print("xx=%d, x0=%d, x1=%d" % (xx,x0,x1))
                    mc.setBlock(xx, y + h, z+w, block.AIR)
                else:
                    mc.setBlock(xx, y + h, z-w, block.AIR)
        else:
            for zz in range((int)(z0)+1, (int)(z1),2):
                if (dir == "e"):
                    mc.setBlock(x-w, y + h, zz, block.AIR)
                else:
                    mc.setBlock(x+w, y + h, zz, block.AIR)

def buildroof(x,y,z,w,h):
    w = round(w)

    mc.setBlocks(x-w+1,y+h,z-w+1,x+w-1,y+h,z+w-1, block.STONE_BRICK.id, 0)

def buildwalls(x,y,z,width,height,battlements=True, roof=False):
    buildwall(x,y,z, width/2, height, "n", battlements, not roof)
    buildwall(x,y,z, width/2, height, "s", battlements, not roof)
    buildwall(x,y,z, width/2, height, "w", battlements, not roof)
    buildwall(x,y,z, width/2, height, "e", battlements, not roof)

    if (roof):
        buildroof(x,y,z, width/2, height-2)

def buildkingdom(x,y,z):
    mc.setBlocks(x - kingdomwidth/2, 1,   z - kingdomwidth/2,
             x + kingdomwidth/2, 100, z + kingdomwidth/2, block.AIR.id)

    mc.setBlocks(x - kingdomwidth/2, 0, z - kingdomwidth/2,
             x + kingdomwidth/2, 0, z + kingdomwidth/2, block.GRASS.id)

def buildwindows(x,y,z,w,h):
    mc.setBlocks(x,y + h/2,z,x,y+h/2,z,block.AIR)

c = mc.player.getPos()
c.x=0
c.y=0
c.z=0

buildkingdom(c.x, c.y, c.z)

w,h=35,7
buildwalls(c.x, c.y, c.z, w, h)
buildstairs(c.x+w/2-h+3,c.y+1, c.z-w/2+1,h-2)
builddoor(c.x+w/2+1,c.y,c.x,2)
buildwindows(c.x+w/2+1,c.y,c.z,w,h)
buildwindows(c.x-w/2,c.y,c.z,w,h)
buildwindows(c.x,c.y,c.z-w/2,w,h)
buildwindows(c.x,c.y,c.z+w/2+1,w,h)

w,h=23,12
buildwalls(c.x, c.y, c.z, w, h)
buildstairs(c.x+w/2-h+3,c.y+1, c.z-w/2+1,h-2)
builddoor(c.x+w/2+1,c.y,c.z,2)
builddoor(c.x-w/2,c.y,c.z,2)
builddoor(c.x,c.y,c.z-w/2,2)
builddoor(c.x,c.y,c.z+w/2+1,2)
buildwindows(c.x+w/2+1,c.y,c.z,w,h)
buildwindows(c.x-w/2,c.y,c.z,w,h)
buildwindows(c.x,c.y,c.z-w/2,w,h)
buildwindows(c.x,c.y,c.z+w/2+1,w,h)

w,h=11,7
yy = c.y
xx = c.x
zz = c.y
floors = 3
for i in range(0,floors):
    print(i)
    buildwalls(c.x, yy, c.z, w, h, (i==floors-1), True)

    if (i>0):
        buildwindows(c.x + w / 2 + 1, yy-1, c.z, w, h)
        buildwindows(c.x - w / 2, yy-1, c.z, w, h)
        buildwindows(c.x, yy-1, c.z - w / 2, w, h)
        buildwindows(c.x, yy-1, c.z + w / 2 + 1, w, h)
    else:
        mc.setBlock(c.x - w/2+1, yy+3, c.z, block.TORCH, 0)
        mc.setBlock(c.x, yy+3, c.z + w/2, block.TORCH, 0)

        #buildwindows(c.x - w / 2, yy-1, c.z, w, h)
        #buildwindows(c.x, yy-1, c.z - w / 2, w, h)
        #buildwindows(c.x, yy-1, c.z + w / 2 + 1, w, h)

    face = ["n", "s", "n"]
    if (i==floors-1 or True):

        if (i == 0):
            hh = h-2
        else:
            hh = h-1

        if (face[i] == "n"):
            xx = c.x + w/2 - hh + 2
            zz = c.z - w/2 + 1
        else:
            xx = c.x + w / 2 - hh + 2
            zz = c.z + w/2

        if (i == 0):
            buildstairs(xx-1, yy + 1, zz, hh)
        else:
            buildstairs(xx-2, yy - 1, zz, hh+1)
    yy+=h
builddoor(c.x+w/2+1,c.y,c.x,2)

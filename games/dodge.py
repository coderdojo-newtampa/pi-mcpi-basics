#
# Run away from the giant cube!!!
#
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time
import mcpi.vec3 as vec3

mc = minecraft.Minecraft.create("192.168.1.5")

gameover = False
enemy = vec3.Vec3(5,10,5)
enemy_size = 1
enemy_speed = 0.25

# Draws enemy block, use draw(vec3, Block.AIR.id) to erase previous position)
def draw(enemyplayer, block=block.WOOL.id):
    mc.setBlocks(
        enemyplayer.x-enemy_size,
        enemyplayer.y-enemy_size,
        enemyplayer.z-enemy_size,
        enemyplayer.x+enemy_size,
        enemyplayer.y+enemy_size,
        enemyplayer.z+enemy_size,
        block, random.randint(0,15))

# Move the enemy block towards the player
def move(enemypos):
    pos = mc.player.getPos()
    old_pos = enemypos.clone()

    if pos.x < enemypos.x:
        enemypos.x -= 1
    elif pos.x > enemypos.x:
        enemypos.x += 1

    if pos.y < enemypos.y:
        enemypos.y -= 1
    elif pos.y > enemypos.y:
        enemypos.y += 1

    if pos.z < enemypos.z:
        enemypos.z -= 1
    elif pos.z > enemypos.z:
        enemypos.z += 1

    draw(enemypos)
    draw(old_pos, block.AIR)

    draw(enemy)

mc.postToChat("Start running from the Cube!!!")

while (not gameover):
    move(enemy)
    pos = mc.player.getPos()

    print(mc.getBlock(pos.x,pos.y,pos.z))

    if (mc.getBlock(pos.x,pos.y,pos.z) == block.WOOL.id):
        gameover = True

    time.sleep(enemy_speed)

mc.postToChat("Game over!!!")
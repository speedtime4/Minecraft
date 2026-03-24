STEP=20
import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=-469
y=1
z=-591
def directionZ():
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+1, pos.y+2, pos.z+4, 5)
    mc.setBlocks(pos.x, pos.y+1, pos.z, pos.x+1, pos.y+2, pos.z, 0)
    mc.setBlocks(pos.x, pos.y+1, pos.z+2, pos.x+1, pos.y+1, pos.z+2, 0)
    mc.setBlocks(pos.x, pos.y+1, pos.z+4, pos.x+1, pos.y+2, pos.z+4, 0)
def directionX():
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+4, pos.y+2, pos.z+1, 5)
    mc.setBlocks(pos.x, pos.y+1, pos.z, pos.x, pos.y+2, pos.z+1, 0)
    mc.setBlocks(pos.x+2, pos.y+1, pos.z, pos.x+2, pos.y+1, pos.z+1, 0)
    mc.setBlocks(pos.x+4, pos.y+1, pos.z, pos.x+4, pos.y+2, pos.z+1, 0)
for i in range(5):
    directionX()
    pos.x+=STEP
    time.sleep(1)
    mc.setBlocks(pos.x-STEP, pos.y, pos.z, pos.x, pos.y+2, pos.z+1, 0)

for i in range(5):
    directionZ()
    pos.z+=STEP
    time.sleep(1)
    mc.setBlocks(pos.x, pos.y, pos.z-STEP, pos.x+1, pos.y+2, pos.z, 0)

for i in range(5):
    directionX()
    pos.x-=STEP
    time.sleep(1)
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+(2*STEP-1), pos.y+2, pos.z+1, 0)
for i in range(5):
    directionZ()
    pos.z-=STEP
    time.sleep(1)
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+1, pos.y+2, pos.z+(2*STEP-1), 0)


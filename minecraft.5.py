import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=70
y=6
s=-222
# x=pos.x
# y=pos.y
# s=pos.z
# for i in range(1,100,10):
#     print(i)
# sun=50
# for i in range(1,11):
#     print(sun*i)
#     print(i)
# mc.setBlock(x+1,y-1,s,53)
# mc.setBlock(x+2,y-1,s,5)
# mc.setBlock(x+2,y,s,53)
# mc.setBlock(x+3,y+1,s,53)
# mc.setBlock(x+3,y-1,s,5)
# mc.setBlock(x+3,y,s,5)
# mc.setBlock(x+3,y,s,53)
# for i in range(1,4):
#     for H in range(i*2):
#         mc.setBlock(x+i,y+H,s,5)
# a=0
# b=0
# for i in range(-1,5,1):
#     mc.setBlocks(x+a,y+b,s,x+i+a,y+b,s,7)
#     a+=2
#     b+=1
# a=0
# b=0
# for i in range(10):
#     mc.setBlock(x+i*4,y,s,0)
#     mc.setBlock(x+i*4+1,y+1,s,5)
# 
# for i in range(1,8,2):
#     mc.setBlock(x+i,y,s,95,15)
#     mc.setBlock(x+i,y,s-1,95)
#     mc.setBlock(x+i,y,s-2,95,15)
#     mc.setBlock(x+i,y,s-3,95)
#     mc.setBlock(x+i,y,s-4,95,15)
#     mc.setBlock(x+i,y,s-5,95)
#     mc.setBlock(x+i,y,s-6,95,15)
#     mc.setBlock(x+i,y,s-7,95)
# for a in range(2,9,2):
#     mc.setBlock(x+a,y,s,95)
#     mc.setBlock(x+a,y,s-1,95,15)
#     mc.setBlock(x+a,y,s-2,95)
#     mc.setBlock(x+a,y,s-3,95,15)
#     mc.setBlock(x+a,y,s-4,95)
#     mc.setBlock(x+a,y,s-5,95,15)
#     mc.setBlock(x+a,y,s-6,95)
#     mc.setBlock(x+a,y,s-7,95,15)
# for i in range(8):
#     for a in range(8):
#         if (i+a)%2==0:
#             mc.setBlock(x+a,y,s+i,95)
#         else:
#             mc.setBlock(x+a,y,s+i,95,15)

# mc.setBlocks(x,y,s,x+10,y,s+10)
# for i in range(9,-1,-1):
#     mc.setBlocks(x-i,y,s-i,x+i,y,s+i,5)
#     y+=1
# mc.setBlocks(x-9,y,s-9,x+9,y,s+9,5)
# mc.setBlocks(x-8,y-1,s-8,x+8,y-1,s+8,5)
# mc.setBlocks(x-7,y-2,s-7,x+7,y-2,s+7,5)
# mc.setBlocks(x-6,y-3,s-6,x+6,y-3,s+6,5)
# mc.setBlocks(x-5,y-4,s-5,x+5,y+4,s+5,5)
# mc.setBlocks(x-4,y-5,s-4,x+4,y+5,s+4,5)
# mc.setBlocks(x-3,y-6,s-3,x+3,y+6,s+3,5)
# mc.setBlocks(x-2,y-7,s-2,x+2,y+7,s+2,5)
# mc.setBlocks(x-1,y-8,s-1,x+1,y+8,s+1,5)
# mc.setBlocks(x-0,y-9,s-0,x+0,y+9,s+0,5)
# p=0
# a=0
# for i in range(30):
#     number=random.randint(0,15)
#     print(number)
#     if a%6==0:
#         a=0
#         p+=1
#     mc.setBlock(x+a,y+p,s,35,number)
#     a+=1
# mc.setBlock(x+1,y,s,35)
# mc.setBlock(x+1,y,s-1,35)
# mc.setBlock(x+1,y,s-2,35,2)
# mc.setBlock(x+1,y+1,s-2,35,4)
# mc.setBlock(x+1,y+1,s-1,35,5)
# mc.setBlock(x+1,y+1,s,35,4)
# mc.setBlock(x+1,y+1,s+1,35)
# mc.setBlock(x+1,y+1,s+2,35,1)
# mc.setBlock(x+1,y,s+2,35,1)
# mc.setBlock(x+1,y,s+1,35,1)
# mc.setBlock(x+1,y+2,s+2,35,4)
# mc.setBlock(x+1,y+2,s+1,35,4)
# mc.setBlock(x+1,y+2,s,35,1)
# mc.setBlock(x+1,y+2,s-1,35)
# mc.setBlock(x+1,y+2,s-2,35,2)
# mc.setBlock(x+1,y+3,s+2,35,2)
# mc.setBlock(x+1,y+3,s+1,35,2)
# mc.setBlock(x+1,y+3,s,35,4)
# mc.setBlock(x+1,y+3,s-1,35)
# mc.setBlock(x+1,y+3,s-2,35)
# mc.setBlock(x+1,y+4,s+2,35,1)
# mc.setBlock(x+1,y+4,s+1,35,4)
# mc.setBlock(x+1,y+4,s,35,4)
# mc.setBlock(x+1,y+4,s-1,35,3)
# mc.setBlock(x+1,y+4,s-2,35)
# i=10
# for i in range(1,5):
#     mc.setBlock(x+1,y,s,35,8)
#     mc.setBlock(x+2,y,s,35,8)
#     mc.setBlock(x+3,y,s,35,8)
#     mc.setBlock(x+1,y,s+1,35,8)
#     mc.setBlock(x+2,y,s+1,35,8)
#     mc.setBlock(x+3,y,s+1,35,8)
#     mc.setBlock(x+1,y,s+2,35,8)
#     mc.setBlock(x+2,y,s+2,35,8)
#     mc.setBlock(x+3,y,s+2,35,8)
#     mc.setBlock(x+2,y+1,s+1,35)
#     mc.setBlock(x+2,y+2,s+1,35)
#     mc.setBlock(x+2,y+3,s+1,35)
#     mc.setBlock(x+2,y+4,s+1,35)
#     mc.setBlock(x+2,y+5,s+1,35,8)
#     mc.setBlock(x+1,y+5,s,35,8)
#     mc.setBlock(x+1,y+5,s+1,35,8)
#     mc.setBlock(x+2,y+5,s,35,8)
#     mc.setBlock(x+3,y+5,s,35,8)
#     mc.setBlock(x+3,y+5,s+1,35,8)
#     mc.setBlock(x+3,y+5,s+2,35,8)
#     mc.setBlock(x+1,y+5,s+2,35,8)
#     mc.setBlock(x+2,y+5,s+2,35,8)
#     x+=10
# for i in range(1,6):
#     mc.setBlocks(x+5,y+4,s+5,x,y,s,41)
#     mc.setBlocks(x+5,y+4,s+5,x,y+8,s,1)
#     mc.setBlock(x,y+7,s+1,251,15)
#     mc.setBlock(x,y+7,s+4,251,15)
#     mc.setBlock(x,y+3,s+1,251,15)
#     mc.setBlock(x,y+4,s+1,251,15)
#     mc.setBlock(x,y+4,s+2,251,15)
#     mc.setBlock(x,y+5,s+2,251,15)
#     mc.setBlock(x,y+5,s+3,251,15)
#     mc.setBlock(x,y+3,s+4,251,15)
#     mc.setBlock(x,y+4,s+4,251,15)
#     mc.setBlock(x,y+4,s+3,251,15)
#     x+=15
# a=0
# for i in range(3):
#     mc.setBlock(x+1+a,y,s,123)
#     mc.setBlock(x+2+a,y+1,s,123)
#     mc.setBlock(x+3+a,y+2,s,123)
#     a+=5
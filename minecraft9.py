import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=-80
y=7
z=-161
def one(x,y,z,block):
    mc.setBlock(x+1,y,z,block)
    mc.setBlock(x+1,y+1,z,block)
    mc.setBlock(x+1,y+2,z,block)
    mc.setBlock(x+1,y+3,z,block)
    mc.setBlock(x+1,y+4,z,block)
    mc.setBlock(x+1,y+3,z+1,block)
    mc.setBlock(x+1,y+2,z+2,block)
one(x,y,z,7)
mc.setBlock(x+1,y,z-2,7)
mc.setBlock(x+1,y,z-3,7)
mc.setBlock(x+1,y,z-4,7)
mc.setBlock(x+1,y+1,z-4,7)
mc.setBlock(x+1,y+2,z-4,7)
mc.setBlock(x+1,y+2,z-3,7)
mc.setBlock(x+1,y+2,z-2,7)
mc.setBlock(x+1,y+3,z-4,7)
mc.setBlock(x+1,y+4,z-4,7)
mc.setBlock(x+1,y+4,z-3,7)
mc.setBlock(x+1,y+4,z-2,7)
one(x=x,y=y,z=z-8,block=5)
# mc.setBlock(x+1,y,z,7)
# mc.setBlock(x+1,y+1,z,7)
# mc.setBlock(x+1,y+2,z,7)
# mc.setBlock(x+1,y+3,z,7)
# mc.setBlock(x+1,y+4,z,7)
# mc.setBlock(x+1,y+3,z+1,7)
# mc.setBlock(x+1,y+2,z+2,7)

# def block():
#     print("как у тебя дела? 😎")
#     print("что делал сегодня? 😀")
# # a=1
# # b=2
# # c=a+b
# # print(c)
# def sumo(a,b):
#     c=a-b
#     return c
# a=sumo(3,4)
# b=sumo(4,4)
# print(a)
# print(b)
# a=1
# if a==1:
#     print("привет первый игрок")
#     print("как у тебя дела? 😉")
# elif a==2:
#     print("привет второй игрок")
#     print("как у тебя дела? 😉")
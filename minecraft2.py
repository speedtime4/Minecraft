# h=10
# if h> 18:
#     print("you can drive a car")
# else:
#     print("you can not drive a car")
# a=10
# if a> 21:
#     print("you can go to park")
# elif a> 18:
#     print("you can go to park mum")
# else:
#     print("you can not go park")
#     print("daniel")
# a=77
# b=15
# c=24
# if a> b:
#     print(a)
# elif b <16:
#     print("16 big")
# else:
#     print("9 big")
# a=1
# b=2
# c=3
# if a> b and a> c:
#     print(a)
# elif b> c and b> a:
#     print("b big")
# else:
    # print("c big")
# a=4
# b=9
# c=3
# d=0
# if a==b:
#     print("a=b")
# elif a==c:
#     print("a=c")
# elif b==c:
#     print("b=c")
# else:
#     print("0")
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
x=30
y=-1
s=-272
# while True:
Block=(mc.getBlock(x,y,s))
# mc.setBlock(x,y,s,46)
if Block==56:
    print("yes")
    mc.setBlocks(x+7,y+7,s+7,x+1,y+1,s+1,5)
    mc.setBlocks(x+6,y+6,s+6,x+2,y+2,s+2,0)
elif Block==7:
    mc.setBlocks(x+7,y+7,s+7,x+1,y+1,s+1,56)
    mc.setBlocks(x+6,y+6,s+6,x+2,y+2,s+2,0)
elif Block==15:
    mc.setBlocks(x+7,y+7,s+7,x+1,y+1,s+1,0)
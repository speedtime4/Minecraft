import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=-372
y=8
z=-142
# bb=-10
# s=[15,1,4,5]
# v=[14,9,3,13]
# while True:
#     aa=random.randint(0,len(s)-1)
#     # mc.setBlock(x+1,y,z,251,s[aa])
#     # aa = random.choice(s)
#     if bb==aa:
#         aa=random.randint(0,len(s)-1)
#     mc.setBlock(x+1,y,z,251,s[aa])
#     mc.setBlock(x+2,y,z,251,v[aa])
#     mc.setBlock(x+3,y,z,251,s[aa])
#     mc.setBlock(x+4,y,z,251,v[aa])
#     mc.setBlock(x+5,y,z,251,s[aa])
#     mc.setBlock(x+6,y,z,251,v[aa])
#     mc.setBlock(x+7,y,z,251,s[aa])
#     mc.setBlock(x+8,y,z,251,v[aa])
#     mc.setBlock(x+9,y,z,251,s[aa])
# #     mc.setBlock(x+10,y,z,251,v[aa])
# #     bb=aa
# #     time .sleep(1)
# a=[
# [1,2,3,4],
# [11,12,13,14],
# [21,22,23,24],
# [31,32,33,34]
# ]
# # a[2].append(25)
# # a.append([41,42,43,44])
# # print(a)
# # print(a[2][3])
# # a[1].insert(0,10)
# # print(a)
# # a[0].pop(0)
# # print(a)
# # a.remove([1,2,3,4])
# # print(a)
# a.append([0,0,0,0])
# print(a)
# a.insert(2,[4,4,4,4])
# print(a)
a=[]
for i in range(10):
    c=[]
    for k in range(5):
        b=random.randint(1,10)
        c.append(b)
    a.append(c)
print(a)
# mc.setBlock(x+1,y,z,5)
# a=[]
# for i in range(10):
#     b=random.randint(1,4)
#     a.append(b)
# print(a)
# start=x
# for i in a:
#     for color in i:
#         # print(i)
#         # print(color)
#         mc.setBlock(x,y,z,color)
#         x+=1
#     x=start
#     y+=1

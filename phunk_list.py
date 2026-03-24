import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=181
y=0
z=-198
# mc.setBlock(x+1,y,z,22)
# mc.setBlock(x+1,y+1,z,22)
# mc.setBlock(x+1,y+2,z,22)
# mc.setBlock(x+1,y+3,z,22)
# mc.setBlock(x+1,y+4,z,22)

# mc.setBlock(x+1,y+5,z,20)
# mc.setBlock(x+1,y+6,z,20)
# mc.setBlock(x+1,y+7,z,20)
# mc.setBlock(x+1,y+8,z,20)
# mc.setBlock(x+1,y+9,z,20)
# for i in range(10):
#     # mc.setBlock(x,y+i,z,22)
# a=[20,20,20,20,20,20,20,20,20,20]
# # for i in range(10):
# #     a.append(21)
# #     print(a)
# c=0
# while True:
#     c+=1
#     if c>len(a)-1:
#         c=0
#     color=random.randint(0,15)
#     a[c]=color
#     mc.setBlock(x+1,y,z,35,a[0])
#     mc.setBlock(x+1,y+1,z,35,a[1])
#     mc.setBlock(x+1,y+2,z,35,a[2])
#     mc.setBlock(x+1,y+3,z,35,a[3])
#     mc.setBlock(x+1,y+4,z,35,a[4])

#     mc.setBlock(x+1,y+5,z,35,a[5])
#     mc.setBlock(x+1,y+6,z,35,a[6])
#     mc.setBlock(x+1,y+7,z,35,a[7])
#     mc.setBlock(x+1,y+8,z,35,a[8])
#     mc.setBlock(x+1,y+9,z,35,a[9])
#     time .sleep(1)
    # b=random.randint(0,9)

# b=15
# def points(anser,all):
#     mypoints=anser/all*100
#     return mypoints
# mypoints=points(all=a,anser=b)
# print(mypoints)
# def getmoney(points):
#     if points>90:
#         print("100$")
#     elif points>80:
#         print("80$")
#     elif points>70:
#         print("50$")
#     elif points<65:
#         print("-25$")
# getmoney(mypoints)
# a=["картошка","вода","свекла"]
# print(a)
# # a.append("капуста")
# # print(a)
# # a[1]="морковь"
# # print(a)
# # a.remove("картошка")
# # print(a)
# a.pop(0)
# print(a)
# v=[]
# for i in range(2,101,2):
#     v.append(i)
# print(v)
# a = [29, 14, 78, 34, 92, 65, 24, 11, 91, 73]
# b=0
# for i in a:
#     # if i>27 and i<93:
#     #     print(i)
#     if i<50:
#         b+=i
#         print(i)
#     print(b)
# for i in a:
#     if i>50 and i<80:
#         print(i)
# c=0
# b=0
# a = [1,2,3,4,5,6,7,8,9,10,16,-11,-12,-13,-14]
# for i in a:
#     if i<0:
#         c=c+i
#         print(i)
#     else:
#         b=b+1
# print([b,c])
# v = [1,2,3,4,5,-1,-2,-3,-4,-5]
# b = []
# for i in v:
#     print(i*-1)
#     b.append(i*-1)
# print(v)
# print(b)
# v = [687,567,-265,-985,485,900,333,-750]
# # for i in range(len(v)):
# #     # print(i)
# #     v[i]=v[i]*-1
# #     print(v[i])
# # print(len(v))
# # print(v)
# c=0
# for i in v :
#     if i>0:
#         c=c+i
# print(c)

# d=0
# for i in range(len(v)):
#     if v[i]>0:
#         d=d+v[i]
# print(d)

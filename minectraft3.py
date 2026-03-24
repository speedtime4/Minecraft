import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=43
y=3
s=-199
# mc.setBlock(x,y,s,20)
# mc.setBlock(x,y,s+1,5)
# mc.setBlock(x,y+1,s+1,5)
# mc.setBlock(x-1,y+1,s+1,5)
# mc.setBlock(x-1,y,s+1,5)
# Block=(mc.getBlock(x,y,s))
# print(Block)
# if Block==122:
#     mc.setBlock(x,y,s+1,0)
#     mc.setBlock(x,y+1,s+1,0)
#     mc.setBlock(x-1,y+1,s+1,0)
#     mc.setBlock(x-1,y,s+1,0)
# elif Block==20:
#     print("No")
# else:
#     print("No_1")
# if Block==129:
#     print("yes")
#     mc.setBlocks(x+1,y+1,s,x,y,s,0)
# elif Block==7:
#     mc.setBlock(x,y,s+1,7)
#     mc.setBlock(x,y+1,s+1,7)
#     mc.setBlock(x-1,y+1,s+1,7)
#     mc.setBlock(x-1,y,s+1,7)
# else:
#     print("No_1")
# if Block==41:
#     print("yes")
#     mc.setBlock(x,y,s+1,57)
#     mc.setBlock(x,y+1,s+1,57)
#     mc.setBlock(x-1,y+1,s+1,57)
#     mc.setBlock(x-1,y,s+1,57)
# elif Block==57:
#     mc.setBlock(x,y,s+1,41)
#     mc.setBlock(x,y+1,s+1,41)
#     mc.setBlock(x-1,y+1,s+1,41)
#     mc.setBlock(x-1,y,s+1,41)
#     print("No_1")
# dak=input("Type something")
# if dak=="yes":

#     mc.setBlock(x+1,y-1,s,56)
#     mc.setBlock(x+2,y-1,s,56)
#     mc.setBlock(x+3,y-1,s,56)
#     mc.setBlock(x+4,y-1,s,56)
#     mc.setBlock(x+5,y-1,s,56)
#     mc.setBlock(x+5,y-1,s+1,56)
#     mc.setBlock(x+5,y-1,s+2,56)
#     mc.setBlock(x+5,y-1,s+3,56)
#     mc.setBlock(x+5,y-1,s+4,56)
#     mc.setBlock(x+5,y-1,s+5,56)
#     mc.setBlock(x+4,y-1,s+5,56)
# elif dak==("not"):

#     mc.setBlock(x+1,y,s,41)
#     mc.setBlock(x+2,y,s,41)
#     mc.setBlock(x+3,y,s,41)
#     mc.setBlock(x+4,y,s,41)
#     mc.setBlock(x+5,y,s,41)
#     mc.setBlock(x+5,y,s+1,41)
#     mc.setBlock(x+5,y,s+2,41)
#     mc.setBlock(x+5,y,s+3,41)
#     mc.setBlock(x+5,y,s+4,41)
#     mc.setBlock(x+5,y,s+5,41)
#     mc.setBlock(x+4,y,s+5,41)
#     mc.setBlock(x+3,y,s+5,41)
#     mc.setBlock(x+2,y,s+5,41)
#     mc.setBlock(x+1,y,s+5,41)
#     mc.setBlock(x+1,y,s+4,41)
#     mc.setBlock(x+1,y,s+3,41)
#     mc.setBlock(x+1,y,s+2,41)
#     mc.setBlock(x+1,y,s+1,41)
# else:

#     mc.setBlock(x+1,y,s,129)
#     mc.setBlock(x+2,y,s,129)
#     mc.setBlock(x+3,y,s,129)
#     mc.setBlock(x+4,y,s,129)
#     mc.setBlock(x+5,y,s,129)
#     mc.setBlock(x+1,y+1,s,129)
#     mc.setBlock(x+1,y+2,s,129)
#     mc.setBlock(x+1,y+3,s,129)
#     mc.setBlock(x+1,y+4,s,129)
#     mc.setBlock(x+2,y+4,s,129)
#     mc.setBlock(x+3,y+4,s,129)
#     mc.setBlock(x+4,y+4,s,129)
#     mc.setBlock(x+5,y+4,s,129)
#     mc.setBlock(x+5,y+3,s,129)
#     mc.setBlock(x+5,y+2,s,129)
#     mc.setBlock(x+5,y+1,s,129)
#     mc.setBlock(x+5,y+6,s,129)
#     mc.setBlock(x+5,y+7,s,129)
#     mc.setBlock(x+4,y+7,s,129)
#     mc.setBlock(x+3,y+7,s,129)
#     mc.setBlock(x+2,y+7,s,129)
#     mc.setBlock(x+1,y+7,s,129)
# dak=7
# if dak==1:
#     print("Monday")
# elif dak==2:
#     print("Tuesday")
# elif dak==3:
#     print("Wednesday")
# elif dak==4:
#     print("Thursday")
# elif dak==5:
#     print("Friday")
# elif dak==6:
#     print("Saturday")
# elif dak==7:
#     print("Sunday")
# else:
#     print("1.7")
login="Speed_Time"
password="575757"
login1= input("login")
if login1==login:
    print("yes")
    password1= input("password")
    if password1==password:
        print("yes")
    else:
        print("not222")
    print("YYYYYYY")
else:
    print("not111")
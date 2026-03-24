import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=202
y=0
z=-151
# mc.setBlock(x,y,s,251)
# mc.setBlock(x+1,y,s,251)
# mc.setBlock(x+2,y,s,251)
# mc.setBlock(x,y,s+1,251)
# mc.setBlock(x+1,y,s+1,251)
# mc.setBlock(x+2,y,s+1,251)
# mc.setBlock(x+1,y,s+2,251)
# mc.setBlock(x+2,y,s+2,251)
# mc.setBlock(x,y,s+2,251)
# mc.setBlock(x,y+1,s,251,8)
# mc.setBlock(x+1,y+1,s,251,8)
# mc.setBlock(x+2,y+1,s,251,8)
# mc.setBlock(x+2,y+1,s+1,251,8)
# mc.setBlock(x+2,y+1,s+2,251,8)
# mc.setBlock(x,y+2,s,251,8)
# mc.setBlock(x+1,y+2,s,251,8)
# mc.setBlock(x+2,y+2,s,251,8)
# mc.setBlock(x+2,y+2,s+1,251,8)
# mc.setBlock(x+2,y+2,s+2,251,8)
# mc.setBlock(x,y+3,s,251,8)
# mc.setBlock(x+1,y+3,s,251,8)
# mc.setBlock(x+2,y+3,s,251,8)
# mc.setBlock(x+2,y+3,s+1,251,8)
# mc.setBlock(x+2,y+3,s+2,251,8)
# mc.setBlock(x,y+4,s,251,8)
# mc.setBlock(x+1,y+4,s,251,8)
# mc.setBlock(x+2,y+4,s,251,8)
# mc.setBlock(x+2,y+4,s+1,251,8)
# mc.setBlock(x+2,y+4,s+2,251,8)
# mc.setBlock(x,y+5,s,251,8)
# mc.setBlock(x+1,y+5,s,251,8)
# mc.setBlock(x+2,y+5,s,251,8)
# mc.setBlock(x+2,y+5,s+1,251,8)
# mc.setBlock(x+2,y+5,s+2,251,8)
# mc.setBlock(x+1,y+5,s+1,251)
# mc.setBlock(x+1,y+4,s+1,198)
# mc.setBlock(x,y+1,s+1,160,8)
# mc.setBlock(x,y+2,s+1,160,8)
# mc.setBlock(x,y+3,s+1,160,8)
# mc.setBlock(x,y+4,s+1,160,8)
# mc.setBlock(x,y+5,s+1,160,8)
# mc.setBlock(x,y+1,s+2,160,8)
# mc.setBlock(x+1,y+2,s+2,160,8)
# mc.setBlock(x+1,y+3,s+2,160,8)
# mc.setBlock(x+1,y+4,s+2,160,8)
# mc.setBlock(x+1,y+5,s+2,160,8)  
# while True:
#     pos=mc.player.getTilePos()
#     if pos.x==143 and pos.y==2 and pos.z==60:
#         print("------1-------")
#         mc.setBlock(pos.x,pos.y+2,pos.z,9)
#     else:
#         if mc.getBlock(143,4,60)!=0:

#             print("------2-------")
#             mc.setBlock(143,4,60,0)
#             mc.setBlock(143,3,60,0)
#         else:
#             mc.setBlock(143,4,60,46)
#             print("------3-------")
#     time.sleep(2)
# mc.player.setTilePos(38,1,60)
# time.sleep(5)
# mc.player.setTilePos(27,1,45)
# time.sleep(5)
# mc.player.setTilePos(32,2,21)
# time.sleep(5)
# mc.player.setTilePos(59,23,0)
# time.sleep(5)
# mc.player.setTilePos(30,7,-11)
# time.sleep(5)
# mc.player.setTilePos(38,1,60)
# while True:
#     pos=mc.player.getTilePos()
#     Block=(mc.getBlock(pos.x,pos.y-1,pos.z))
#     # mc.setBlock(pos.x,pos.y-1,pos.z,56)
#     if Block!=0 and Block!=8 and Block!=9:
#         mc.setBlock(pos.x,pos.y-1,pos.z,56)
    
    # if Block==8:
    #     mc.setBlock(pos.x,pos.y-1,pos.z,8)

    # if Block==9:
    #     mc.setBlock(pos.x,pos.y,pos.z,9)
    #     print(Block)
    #     print(pos)

    # time.sleep (1) 

# while True:
#     pos=mc.player.getTilePos()
#     number=random.randint(0,15)
#     # if pos.x==167 and pos.y==3 and pos.z==72:
#     if pos.x>=x and pos.x<=x+5 and pos.y==y+1 and pos.z>=s and pos.z<=s+5: 
#         mc.setBlocks(x,y,s,x+5,y,s+5,35,number)
#         print(pos)
#     time.sleep(1)
# for i in range(3):
#         numberx=random.randint(-4,4)
#         numbery=random.randint(0,4)
#         numberz=random.randint(-4,4)
#         mc.setBlock(x+numberx,y+numbery,z+numberz,46)


# TNT=3       
# while True:
#     pos=mc.player.getTilePos()
#     Block=(mc.getBlock(pos.x,pos.y-1,pos.z)) 
#     if Block==46:
#         mc.postToChat(TNT)
#         TNT-=1
#         time.sleep(1)
#     else:
#         TNT=3
#         time.sleep(1)
#     if TNT==0:
#         mc.postToChat("Boom")
#         pos=mc.player.getTilePos()
#         print(pos)
#         x=pos.x
#         y=pos.y
#         z=pos.z
#         mc.setBlocks(x,y,z,x+4,y-10,z+4,0)
#         break

# mc.setBlock(x+1,y,z,41)
# mc.setBlock(x+2,y,z,41)
# mc.setBlock(x+3,y,z,41)
# mc.setBlock(x+4,y,z,41)
# mc.setBlock(x+5,y,z,41)
# mc.setBlock(x+6,y,z,41)
# mc.setBlock(x+7,y,z,41)
# mc.setBlock(x+7,y,z+1,41)
# mc.setBlock(x+6,y,z+1,0)
# mc.setBlock(x+5,y,z+1,41)
# mc.setBlock(x+4,y,z+1,0)
# mc.setBlock(x+3,y,z+1,41)
# mc.setBlock(x+2,y,z+1,0)
# mc.setBlock(x+1,y,z+1,41)
# mc.setBlock(x+7,y,z+2,41)
# mc.setBlock(x+6,y,z+2,41)
# mc.setBlock(x+5,y,z+2,41)
# mc.setBlock(x+4,y,z+2,41)
# mc.setBlock(x+3,y,z+2,41)
# mc.setBlock(x+2,y,z+2,41)
# mc.setBlock(x+1,y,z+2,41)
# mc.setBlock(x+7,y,z+3,41)
# mc.setBlock(x+6,y,z+3,0)
# mc.setBlock(x+5,y,z+3,41)
# mc.setBlock(x+4,y,z+3,0)
# mc.setBlock(x+3,y,z+3,41)
# mc.setBlock(x+2,y,z+3,0)
# mc.setBlock(x+1,y,z+3,41)
# mc.setBlock(x+7,y,z+4,41)
# mc.setBlock(x+6,y,z+4,41)
# mc.setBlock(x+5,y,z+4,41)
# mc.setBlock(x+4,y,z+4,41)
# mc.setBlock(x+3,y,z+4,41)
# mc.setBlock(x+2,y,z+4,41)
# mc.setBlock(x+1,y,z+4,41)
# mc.setBlock(x+7,y,z+5,41)
# mc.setBlock(x+6,y,z+5,0)
# mc.setBlock(x+5,y,z+5,41)
# mc.setBlock(x+4,y,z+5,0)
# mc.setBlock(x+3,y,z+5,41)
# mc.setBlock(x+2,y,z+5,0)
# mc.setBlock(x+1,y,z+5,41)
# mc.setBlock(x+7,y,z+6,41)
# mc.setBlock(x+6,y,z+6,41)
# mc.setBlock(x+5,y,z+6,41)
# mc.setBlock(x+4,y,z+6,41)
# mc.setBlock(x+3,y,z+6,41)
# mc.setBlock(x+2,y,z+6,41)
# mc.setBlock(x+1,y,z+6,41)
s=14
q=0
cell1=0
cell2=0
cell3=0
cell4=0
cell5=0
cell6=0
cell7=0
cell8=0
cell9=0
WINER=0
while True:
    q=int(input("Введите число от 1 до 9: "))
    if cell1==0 and q==1:
        mc.setBlock(x+6,y,z+1,251,s)
        cell1=s
    elif cell2==0 and q==2:
        mc.setBlock(x+4,y,z+1,251,s)
        cell2=s
    elif cell3==0 and q==3:
        mc.setBlock(x+2,y,z+1,251,s)
        cell3=s
    elif cell4==0 and q==4:
        mc.setBlock(x+6,y,z+3,251,s)
        cell4=s
    elif cell5==0 and q==5:
        mc.setBlock(x+4,y,z+3,251,s)
        cell5=s
    elif cell6==0 and q==6:
        mc.setBlock(x+2,y,z+3,251,s)
        cell6=s
    elif cell7==0 and q==7:
        mc.setBlock(x+6,y,z+5,251,s)
        cell7=s
    elif cell8==0 and q==8:
        mc.setBlock(x+4,y,z+5,251,s)
        cell8=s
    elif cell9==0 and q==9:
        mc.setBlock(x+2,y,z+5,251,s)
        cell9=s
    if s==14:
        s=11
    else:
        s=14
    if cell1==cell2==cell3!=0:
        print("WINER 🥇 1")
        WINER=cell1
        break
    if cell8==cell5==cell2!=0:
        print("WINER 🥇 2")
        WINER=cell2
        break
    if cell3==cell6==cell9!=0:
        print("WINER 🥇 3")
        WINER=cell3
        break
    if cell1==cell4==cell7!=0:
        print("WINER 🥇 4")
        WINER=cell4
        break
    if cell3==cell5==cell7!=0:
        print("WINER 🥇 5")
        WINER=cell5
        break
    if cell9==cell5==cell1!=0:
        WINER=cell9
        print("WINER 🥇 6")
        break
    if cell9==cell8==cell7!=0:
        WINER=cell7
        print("WINER 🥇 7")
        break
    if cell4==cell5==cell6!=0:
        print("WINER 🥇 8")
        WINER=cell6
        break
    if cell1!=0 and cell2!=0 and cell3!=0 and cell4!=0 and cell5!=0 and cell6!=0 and cell7!=0 and cell8!=0 and cell9!=0:
        print("ничья")
        break
if WINER==14:
    print(WINER, "крестик")
if WINER==11:
    print(WINER, "нолик")

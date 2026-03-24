import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=202
y=0
z=-151
mc.setBlock(x+1,y,z,41)
mc.setBlock(x+2,y,z,41)
mc.setBlock(x+3,y,z,41)
mc.setBlock(x+4,y,z,41)
mc.setBlock(x+5,y,z,41)
mc.setBlock(x+6,y,z,41)
mc.setBlock(x+7,y,z,41)
mc.setBlock(x+7,y,z+1,41)
mc.setBlock(x+6,y,z+1,0)
mc.setBlock(x+5,y,z+1,41)
mc.setBlock(x+4,y,z+1,0)
mc.setBlock(x+3,y,z+1,41)
mc.setBlock(x+2,y,z+1,0)
mc.setBlock(x+1,y,z+1,41)
mc.setBlock(x+7,y,z+2,41)
mc.setBlock(x+6,y,z+2,41)
mc.setBlock(x+5,y,z+2,41)
mc.setBlock(x+4,y,z+2,41)
mc.setBlock(x+3,y,z+2,41)
mc.setBlock(x+2,y,z+2,41)
mc.setBlock(x+1,y,z+2,41)
mc.setBlock(x+7,y,z+3,41)
mc.setBlock(x+6,y,z+3,0)
mc.setBlock(x+5,y,z+3,41)
mc.setBlock(x+4,y,z+3,0)
mc.setBlock(x+3,y,z+3,41)
mc.setBlock(x+2,y,z+3,0)
mc.setBlock(x+1,y,z+3,41)
mc.setBlock(x+7,y,z+4,41)
mc.setBlock(x+6,y,z+4,41)
mc.setBlock(x+5,y,z+4,41)
mc.setBlock(x+4,y,z+4,41)
mc.setBlock(x+3,y,z+4,41)
mc.setBlock(x+2,y,z+4,41)
mc.setBlock(x+1,y,z+4,41)
mc.setBlock(x+7,y,z+5,41)
mc.setBlock(x+6,y,z+5,0)
mc.setBlock(x+5,y,z+5,41)
mc.setBlock(x+4,y,z+5,0)
mc.setBlock(x+3,y,z+5,41)
mc.setBlock(x+2,y,z+5,0) 
mc.setBlock(x+1,y,z+5,41)
mc.setBlock(x+7,y,z+6,41)
mc.setBlock(x+6,y,z+6,41)
mc.setBlock(x+5,y,z+6,41)
mc.setBlock(x+4,y,z+6,41)
mc.setBlock(x+3,y,z+6,41)
mc.setBlock(x+2,y,z+6,41)
mc.setBlock(x+1,y,z+6,41)
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
    if WINER==0:
        if cell1==0:
            block,color=mc.getBlockWithData(x+2,y,z+5)
            cell1=color 
            # time.sleep(1)
            
        else:
            mc.setBlock(x+2,y,z+5,251,cell1)
            # time.sleep(1)

        if cell2==0:
            block,color=mc.getBlockWithData(x+4,y,z+5)
            cell2=color 
            # time.sleep(1)

        else:
            mc.setBlock(x+4,y,z+5,251,cell2)
            # time.sleep(1)

        if cell3==0:
            block,color=mc.getBlockWithData(x+6,y,z+5)
            cell3=color 
            # time.sleep(1)

        else:
            mc.setBlock(x+6,y,z+5,251,cell3)
            # time.sleep(1)

        if cell4==0:
            block,color=mc.getBlockWithData(x+2,y,z+3)
            cell4=color 
            # time.sleep(1)

        else:
            mc.setBlock(x+2,y,z+3,251,cell4)
            # time.sleep(1)

        if cell5==0:
            block,color=mc.getBlockWithData(x+4,y,z+3)
            cell5=color 
            # time.sleep(1)
        
        else:
            mc.setBlock(x+4,y,z+3,251,cell5)
            # time.sleep(1)

        if cell6==0:
            block,color=mc.getBlockWithData(x+6,y,z+3)
            cell6=color 
            # time.sleep(1)

        else:
            mc.setBlock(x+6,y,z+3,251,cell6)
            # time.sleep(1)

        if cell7==0:
            block,color=mc.getBlockWithData(x+2,y,z+1)
            cell7=color 
            print(cell7)
            # time.sleep(1)

        else:
            mc.setBlock(x+2,y,z+1,251,cell7)
            print(cell7)
            # time.sleep(1)

        if cell8==0:
            block,color=mc.getBlockWithData(x+4,y,z+1)
            cell8=color 
        # time.sleep(1)

        else:
            mc.setBlock(x+4,y,z+1,251,cell8)
            # time.sleep(1)

        if cell9==0:
            block,color=mc.getBlockWithData(x+6,y,z+1)
            cell9=color  
            # time.sleep(1)

        else:
            mc.setBlock(x+6,y,z+1,251,cell9)
        time.sleep(1)

        if cell1==cell2==cell3!=0:
            print("WINER 🥇 1")
            WINER=cell1
            
        if cell8==cell5==cell2!=0:
            print("WINER 🥇 2")
            WINER=cell2
            
        if cell3==cell6==cell9!=0:
            print("WINER 🥇 3")
            WINER=cell3
            
        if cell1==cell4==cell7!=0:
            print("WINER 🥇 4")
            WINER=cell4
            
        if cell3==cell5==cell7!=0:
            print("WINER 🥇 5")
            WINER=cell5
            
        if cell9==cell5==cell1!=0:
            WINER=cell9
            print("WINER 🥇 6")
        
        if cell9==cell8==cell7!=0:
            WINER=cell7
            print("WINER 🥇 7")
            
        if cell4==cell5==cell6!=0:
            print("WINER 🥇 8")
            WINER=cell6
            
        if cell1!=0 and cell2!=0 and cell3!=0 and cell4!=0 and cell5!=0 and cell6!=0 and cell7!=0 and cell8!=0 and cell9!=0:
            print("ничья")
            WINER=-1

    if WINER!=0:
        if WINER==14:
            mc.postToChat("WINER крестик,для рестарта поставте дубовые доски")
            time.sleep(1)
        if WINER==11:
            mc.postToChat("WINER нолик,для рестарта поставте дубовые доски")
            time.sleep(1)
        if WINER==-1:
            mc.postToChat("ничья,для рестарта поставте дубовые доски")
            time.sleep(1)
        a=206
        b=3
        c=-144
        d=mc.getBlock(a,b,c)
        if d==5:
            print("bedrock")
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
            mc.setBlock(x+2,y,z+5,0)
            mc.setBlock(x+4,y,z+5,0)
            mc.setBlock(x+6,y,z+5,0)
            mc.setBlock(x+2,y,z+3,0)
            mc.setBlock(x+4,y,z+3,0)
            mc.setBlock(x+6,y,z+3,0)
            mc.setBlock(x+2,y,z+1,0)
            mc.setBlock(x+4,y,z+1,0)
            mc.setBlock(x+6,y,z+1,0)
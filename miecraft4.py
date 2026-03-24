import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=27
y=1
s=-177
dak= input ("хотите ли вы построить дом?")
if dak=="yes":
    her=input("какой дом вы хотите построить? большой маленький или 1 блок")
    if her=="big":
        print("ты построил большой дом")
        mc.setBlocks(x,y,s,x+9,y+9,s+9,0)
        mc.setBlocks(x+1,y+1,s+1,x+8,y+8,s+8,0)
    elif her=="normale":
        print("ты построил обычный дом")
        mc.setBlocks(x+6,y+6,s+6,x,y,s,0)
        mc.setBlocks(x+1,y+1,s+1,x+5,y+5,s+5,0)
    else:
        print("кубик")
        mc.setBlock(x+1,y,s,5)

else:
    print("yes")
    sun= input ("хотите построить бассейн?")
    if sun=="yes":
        rer= input ("какой бассейн вы хотите построить? большой маленький 1 кубик")
        if rer=="big":
            print ("ты построил большой бассейн")
            mc.setBlocks(x+10,y+10,s+10,x,y,s,0)
            mc.setBlocks(x+9,y+9,s+9,x+1,y+1,s+1,0)
        elif rer=="normale":
            print ("ты построил обычный бассейн")
            mc.setBlocks(x+5,y+5,s+5,x,y,s,0)
            mc.setBlocks(x+4,y+4,s+4,x+1,y+1,s+1,0)
        else:
            print("кубик")
            mc.setBlock(x+1,y,s,5)
    else:
        huh= input("хотите телепортироватся?")
        if huh=="yes":
            print("телепорт")
            mc.player.setTilePos(30,5,-181)
        else:
            print("вы отказались от любых действий")
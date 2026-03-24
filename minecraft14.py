import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
x=-684
y=1
z=-493
mc.setBlocks(x+1,y,z,x+16,y,z+9,45)
mc.setBlocks(x+15,y,z+8,x+2,y,z+1,0)
a=0
b=5
c=41
d=0
count=5
def game_fild(d,c):
    while d!=count:
        goldx=random.randint(2,14)
        goldz=random.randint(1,8)
        if mc.getBlock(goldx+x,y,goldz+z)!=c:
            d+=1
            mc.setBlock(goldx+x,y,goldz+z,c)
    return d 
while True:
    pos=mc.player.getTilePos()
    if pos.x>=x+1 and pos.x<x+17 and pos.y<=y+10 and pos.z>=z and pos.z<z+9:
        if a==1:
            b=b-0.1
            if mc.getBlock(pos.x,pos.y-1,pos.z)==41:
                mc.setBlock(pos.x,pos.y-1,pos.z,0) 
                count-=1
                if count==0:
                    mc.postToChat("Вы выиграли 😉")
                    break
            mc.postToChat("осталось "+str(round(b,1)))
            time.sleep(0.1)
        else:
            mc.postToChat ("Время запустилось")
            a=1
            d=game_fild(d,c)
    else:
        if a==0:
            mc.postToChat("для начало игры войдите в рамку")
            time.sleep(5)
        else:
            mc.postToChat("Вы вышли за рамку но время время уменшается 😢")
            mc.postToChat("осталось "+str(round(b,1)))
            b=b-0.1
            time.sleep(0.1)
    if b<=0:
        mc.postToChat("вы проиграли 😢")
        break
import random
import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
x=196
y=0
z=-170
mc.setBlock(x+1,y,z,1)
mc.setBlock(x+2,y,z,1)
mc.setBlock(x+3,y,z,1)
mc.setBlock(x+4,y,z,1)
mc.setBlock(x+5,y,z,1)
mc.setBlock(x+6,y,z,1)
mc.setBlock(x+7,y,z,1)
mc.setBlock(x+8,y,z,1)
mc.setBlock(x+9,y,z,1)
mc.setBlock(x+10,y,z,1)
mc.setBlock(x+11,y,z,1)
mc.setBlock(x+12,y,z,1)
mc.setBlock(x+13,y,z,1)
mc.setBlock(x+14,y,z,1)
mc.setBlock(x+15,y,z,1)
mc.setBlock(x+16,y,z,1)
mc.setBlock(x+17,y,z,1)
mc.setBlock(x+18,y,z,1)
mc.setBlock(x+19,y,z,1)
mc.setBlock(x+20,y,z,1)
mc.setBlock(x+1,y,z+1,1)
mc.setBlock(x+2,y,z+1,1)
mc.setBlock(x+3,y,z+1,1)
mc.setBlock(x+4,y,z+1,1)
mc.setBlock(x+5,y,z+1,1)
mc.setBlock(x+6,y,z+1,1)
mc.setBlock(x+7,y,z+1,1)
mc.setBlock(x+8,y,z+1,1)
mc.setBlock(x+9,y,z+1,1)
mc.setBlock(x+10,y,z+1,1)
mc.setBlock(x+11,y,z+1,1)
mc.setBlock(x+12,y,z+1,1)
mc.setBlock(x+13,y,z+1,1)
mc.setBlock(x+14,y,z+1,1)
mc.setBlock(x+15,y,z+1,1)
mc.setBlock(x+16,y,z+1,1)
mc.setBlock(x+17,y,z+1,1)
mc.setBlock(x+18,y,z+1,1)
mc.setBlock(x+19,y,z+1,1)
mc.setBlock(x+20,y,z+1,1)
mc.setBlock(x+1,y+1,z+1,251,14)
mc.setBlock(x+1,y+1,z,251,11)
sunny1=random.randint(2,7)
sunny2=random.randint(8,15)
sunny3=random.randint(16,20)
a=0
player=1
red=1
blue=1
# mc.setBlock(x+2,y+1,z+1,251,14)
# mc.setBlock(x+2,y+1,z,251,11)
while True:
    if player==1:
        print("сейчас ходит первый игрок")
    else:
        print("сейчас ходит второй игрок")
    print("ваш ход")
    b=input("вы готовы кинуть кубик?")
    if b!="yes":
        print("ход переходит следующего")
        if player==1:
            player=2
        else:
            player=1
        continue

    if player==1:


        a=random.randint(1,6)
        print("первый игрок походил на шаг",a)
        mc.setBlock(x+red,y+1,z,0)
        red+=a
        if red==sunny1:
            number=random.randint(1,4)
            red-=number

            print("вы отошли на",number)
        elif red==sunny2:
            number=random.randint(1,4)
            print("вы отошли на",number)
            red-=number
        elif red==sunny3:
            number=random.randint(1,4)
            red-=number
            print("вы отошли на",number)
        mc.setBlock(x+red,y+1,z,251,14)  
        player=2
    else:
        a=random.randint(1,6)
        print("первый игрок походил на шаг",a)
        mc.setBlock(x+blue,y+1,z+1,0)
        blue+=a
        if blue==sunny1:
            number=random.randint(1,4)
            blue-=number

            print("вы отошли на",number)
        elif blue==sunny2:
            number=random.randint(1,4)
            print("вы отошли на",number)
            blue-=number
        elif blue==sunny3:
            number=random.randint(1,4)
            blue-=number
            print("вы отошли на",number)

        mc.setBlock(x+blue,y+1,z+1,251,11)  
        player=1
    time.sleep(1)
    # bedrock=mc.getBlock(x+red,y,z+1)
    # java=mc.setBlock(x+blue,y,z)
    if red>=20:
        print("красный победил🥇")
        break
    if blue>=20:
        print("синий победил🥇")
        break
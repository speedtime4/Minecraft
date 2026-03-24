import mcpi.minecraft as minecraft
import time
mc= minecraft.Minecraft.create()
pos=mc.player.getTilePos()
x=303 
y=0
s=-173 
# mc.postToChat(mc.getBlock(x,y+1,s)==8)
size=10
# mc.player.setTilePos(x,y,s)
mc.setBlocks(x,y,s,x+size,y+size,s+size,5)
mc.setBlocks(x+1,y+1,s+1,x-1+size,y-1+size,s-1+size,0)
c=(pos.y>0 and pos.y <5)
b=(pos.x>303 and pos.x <303+5)
a=(pos.z>-173 and pos.z <-173+5)
print(a==b==c==True)
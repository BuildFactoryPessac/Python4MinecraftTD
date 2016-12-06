from mcpi.minecraft import Minecraft

def displayCoord(x,y,z) :
    print('Coordonnées : {0:2f},{1:2f},{2:2f}'.format(x,y,z))

mc = Minecraft.create()
mc.postToChat ("hello")
pos = mc.player.getPos()
print(pos)

# x --> vers l'Est
# y --> altitude
# z --> vers le Nord
mc.player.setPos(pos.x+5,pos.y,pos.z+5)
x,y,z = mc.player.getPos(96,45,36)

minecraft.py

     

     


from mcpi.minecraft import Minecraft

mc = Minecraft.create()
mc.postToChat ("Teleportation")

#TODO-1 Afficher dans la console la position "brute" du personnage
pos = mc.player.getPos()
mc.postToChat ("Teleportation to ")

#TODO-2 Téléporter le personnage où vous voulez
# x --> vers l'Est
# y --> altitude
# z --> vers le Nord
mc.player.setPos(pos.x+30,pos.y,pos.z+5)
x,y,z = mc.player.getPos()

#TODO-3 Afficher dans la console les coordonnées formattées du personnage
print('Coordonnées : {0:2f},{1:2f},{2:2f}'.format(x,y,z))

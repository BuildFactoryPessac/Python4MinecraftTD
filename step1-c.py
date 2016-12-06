from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

#INFO Déclaration de "constante" pour centraliser les valeurs de la pause
DELAY_SHORT = 0.05
DELAY_MEDIUM = 0.5

#INFO Retarde de 50ms le démarage du programme. A utiliser pour un meilleur visuel
sleep(DELAY_SHORT)

mc = Minecraft.create()

x,y,z = mc.player.getPos()

#TODO-3 Afficher dans la console les coordonnées formattées du personnage
print('Coordonnées : {0:2f},{1:2f},{2:2f}'.format(x,y,z))




#TODO-1 Récupérer dans une variable la position "brute" du personnage
x,y,z = mc.player.getPos()

#TODO-2 Déposer un bloc proche de lui de type "Pierre" --> STONE
mc.setBlock(x,y+10,z,block.STONE.id)
sleep(DELAY_MEDIUM)

#TODO-3 Téléporter le personnage ailleurs
mc.player.setPos(x-5,y,z-5)
sleep(DELAY_MEDIUM)

#TODO-4 Construire un bloc de 2x2x1 proche du personnage
x,y,z = mc.player.getPos()
mc.setBlock(x+1,y,z+1,block.STONE.id)
sleep(DELAY_SHORT)

mc.setBlock(x+2,y,z+2,block.STONE.id)
sleep(DELAY_SHORT)

mc.setBlock(x+1,y,z+2,block.STONE.id)
sleep(DELAY_SHORT)

mc.setBlock(x+2,y,z+1,block.STONE.id)

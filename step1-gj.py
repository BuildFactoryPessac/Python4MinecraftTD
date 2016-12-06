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
direction =  mc.player.getDirection()
#TODO-3 Afficher dans la console les coordonnées formattées du personnage
print('Coordonnées : {0:2f},{1:2f},{2:2f}'.format(x,y,z))
mc.setBlocks(x,y+10,-z,block.DIRT.id)
print direction



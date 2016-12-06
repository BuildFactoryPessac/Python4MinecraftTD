from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from math import floor
    
#INFO DÃ©claration de "constante" pour centraliser les valeurs de la pause
DELAY_SHORT = 0.05
DELAY_MEDIUM = 0.5

#INFO Retarde de 50ms le dÃ©marage du programme. A utiliser pour un meilleur visuel
sleep(DELAY_SHORT)

mc = Minecraft.create()
mc.postToChat ("Construction en masse parametree")

#TODO-1 RÃ©cupÃ©rer la position du personnage
x,y,z = mc.player.getPos()

#TODO-2 Créer une plateforme de 80x80x1 sous le personnage de type "Herbe" --> GRASS
mc.setBlocks(x-40,y-1,z-40,x+40,y-1,z+40,block.GRASS.id)
sleep(DELAY_MEDIUM)

#TODO-3 Coder une méthode teleportCharacter pour déplacer le personnage
def teleportCharacter(dx,dz) :
    tx,ty,tz = mc.player.getPos()
    mc.player.setPos(tx+dx,ty,tz+dz)
    return mc.player.getPos()

#TODO-4 Déplacer le personnage    
x,y,z = teleportCharacter(13,15)

#TODO-5 Coder une méthode createBlockNearMe qui crée un bloc de nxmxp proche de lui de type t
def createBlockNearMe(n,m,p,t) :
    mc.setBlocks(x+1,y,z+1,x+n,y+m-1,z+p,t)

#TODO-6 Créer un bloc de 3x4x5 proche de lui de type "Diamant" : DIAMOND_BLOCK  
createBlockNearMe(3,4,5,block.DIAMOND_BLOCK.id)
sleep(DELAY_MEDIUM)

#TODO-7 Déplacer le personnage    
x,y,z = teleportCharacter(13,15)

#TODO-8 Coder une méthode createCubeNearMe qui crée un cube de n de côté proche de lui de type t
def createCubeNearMe(n,t) :
    createBlockNearMe(n,n,n,t)
    
#TODO-9 Créer un cube de 5 de côté proche de lui de type "Diamant" : DIAMOND_BLOCK  
createCubeNearMe(5,block.DIAMOND_BLOCK.id)
sleep(DELAY_MEDIUM)

#TODO-10 Déplacer le personnage
x,y,z = teleportCharacter(-10,8)

#TODO-11 Coder une méthode createPyramideNearMe qui crée une pyramide de base width proche de lui de type t
def createPyramideNearMe(width,t) :
    tx,ty,tz = mc.player.getPos()

    print ("Création de la pyramide")
    
    if width%2 == 0 :
        width = width+1

    height = (width+1)/2
    halfSize= int(floor(width/2))


    for posy in range(int(ty), int(ty+height)):
        mc.setBlocks(tx-halfSize,posy,tz-halfSize,tx+halfSize,posy,tz+halfSize,t)
        sleep(DELAY_MEDIUM)
        halfSize = halfSize - 1

#TODO-12 Construire une Pyramide de base 7x4x1 proche de lui de type "Or" --> GOLD_BLOCK
createPyramideNearMe(7,block.GOLD_BLOCK.id)

x,y,z = teleportCharacter(18,-14)


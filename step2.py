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

#TODO-2 Créer une plateforme de 80x80x1 sous le personnage de type "Herbe" --> GRASS


#TODO-3 Coder une méthode teleportCharacter pour déplacer le personnage


#TODO-4 Déplacer le personnage    


#TODO-5 Coder une méthode createBlockNearMe qui crée un bloc de nxmxp proche de lui de type t

#TODO-6 Créer un bloc de 3x4x5 proche de lui de type "Diamant" : DIAMOND_BLOCK  


#TODO-7 Déplacer le personnage    

#TODO-8 Coder une méthode createCubeNearMe qui crée un cube de n de côté proche de lui de type t
    
#TODO-9 Créer un cube de 5 de côté proche de lui de type "Diamant" : DIAMOND_BLOCK  

#TODO-10 Déplacer le personnage

#TODO-11 Coder une méthode createPyramideNearMe qui crée une pyramide de base width proche de lui de type t

#TODO-12 Construire une Pyramide de base 7x4x1 proche de lui de type "Or" --> GOLD_BLOCK


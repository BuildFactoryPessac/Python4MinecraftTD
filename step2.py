from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from math import floor
    
#INFO Déclaration de "constante" pour centraliser les valeurs de la pause
DELAY_SHORT = 0.05
DELAY_MEDIUM = 0.5

#INFO Retarde de 50ms le démarage du programme. A utiliser pour un meilleur visuel
sleep(DELAY_SHORT)

mc = Minecraft.create()
mc.postToChat ("Construction en masse parametree")

#TODO-1 Récupérer la position du personnage

#TODO-2 Cr�er une plateforme de 80x80x1 sous le personnage de type "Herbe" --> GRASS


#TODO-3 Coder une m�thode teleportCharacter pour d�placer le personnage


#TODO-4 D�placer le personnage    


#TODO-5 Coder une m�thode createBlockNearMe qui cr�e un bloc de nxmxp proche de lui de type t

#TODO-6 Cr�er un bloc de 3x4x5 proche de lui de type "Diamant" : DIAMOND_BLOCK  


#TODO-7 D�placer le personnage    

#TODO-8 Coder une m�thode createCubeNearMe qui cr�e un cube de n de c�t� proche de lui de type t
    
#TODO-9 Cr�er un cube de 5 de c�t� proche de lui de type "Diamant" : DIAMOND_BLOCK  

#TODO-10 D�placer le personnage

#TODO-11 Coder une m�thode createPyramideNearMe qui cr�e une pyramide de base width proche de lui de type t

#TODO-12 Construire une Pyramide de base 7x4x1 proche de lui de type "Or" --> GOLD_BLOCK


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


mc.postToChat ("Teleportation")

position=mc.player.getPos()
mc.postToChat(position)
blockType=1

#TODO-1 Afficher dans la console la position "brute" du personnage

#TODO-2 Téléporter le personnage où vous voulez
# x --> vers l'Est
# y --> altitude
# z --> vers le Nord


#TODO-3 Afficher dans la console les coordonnées formattées du personnage



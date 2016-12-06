from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
tnt = 46
mc.setBlocks(x+1, y+1, z+1, x+110, y+110, z+110, tnt, 1)


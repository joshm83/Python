from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX =
shwrY =
shwrZ =

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and
    mc.setBlocks(shwrX, shwrY + height, shwrZ,
                 shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shrZ,
                 shwrX + width, shwrY + height, shwrZ + lenth 0)
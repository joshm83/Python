from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Let's make some Golems!")

#This will get the player's position
position = mc.player.getTilePos()

x = position.x
y = position.y
z = position.z

count = 0
while count < 10:

    count += 1

    blockType = 42

    mc.setBlock(x, y, z, blockType)
    y = y + 1

    mc.setBlock(x, y, z, blockType)
    x = x + 1

    mc.setBlock(x, y, z, blockType)
    x = x + -2

    mc.setBlock(x, y, z, blockType)
    x = x + 1
    y = y + 1

    blockType = 91
    mc.setBlock(x, y, z, blockType)

    mc.player.setPos(x + 1, y + 1, z + 1)
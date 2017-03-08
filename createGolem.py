from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#This will get the player's position
position = mc.player.getTilePos()

x = position.x
y = position.y
z = position.z

#Creates the Golem based on the position
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

#This will attempt to set the player to the original position.
x = position.x
y = position.y
z = position.z

mc.player.setTilePos(x, y, z)
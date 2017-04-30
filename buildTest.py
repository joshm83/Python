from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from math import *

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

width = 20
height = 10
length = 12

blockType = 4
air = 0
torch = 50

# This will create a stone building
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

# This will hollow  out the stone building
blockType = air
mc.setBlocks(x + 1, y + 1, z + 1, x + width - 1, y + height - 1, z + length - 1, blockType)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from math import *

pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z
 
width = 14
height = 2
length = 14

#This will build a pool forward and to the right of where ever you are standing.

blockType = 168 #Prismarine
air = 0
water = 8
blue_glass = 95, 3

# This will create a swimming pool
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)

# This will remove the top layer of the box
blockType = air
mc.setBlocks(x + 1, y + 3, z + 1, x + width - 1, y + height - 1, z + length - 1, blockType)

# This will fill the pool with water  out the stone building
blockType = water
mc.setBlocks(x + 1, y + 2, z + 1, x + width - 1, y + height - 1, z + length - 1, blockType)

# This will place a blue stained glass roof over the pool.
blockType = blue_glass
mc.setBlocks(x, y + 3, z, x + width, y + height + 5, z + length, blockType)

# This will hollow  out the blue glass
blockType = air
mc.setBlocks(x + 1, y + 3, z + 1, x + width - 1, y + height +4, z + length - 1, blockType)

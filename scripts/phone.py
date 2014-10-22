import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep

def changed_block(new_block_type):
    print("Changed. New block = " + str(new_block_type))
   # if new_block_type == block.AIR:


def monitor_block(world, block_location):
    [x,y,z] = block_location
    old_block_state = 0
    while True:
	new_block_state = world.getBlock(x, y, z)
	if new_block_state != old_block_state:
	    changed_block(new_block_state)
	    old_block_state = new_block_state
	sleep(0.1)

def connect():
    return minecraft.Minecraft.create("localhost", 4711)

if __name__ == "__main__":
    world = connect()
    print("conected to world")
    block_location = (3, 0.0, 0.0)
    monitor_block(world, block_location)



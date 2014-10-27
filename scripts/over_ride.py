from twitter import Twitter
import ConfigParser as configparser
from twitter import OAuth
from time import sleep
import mcpi.minecraft as minecraft

def connect_to_mc():
    world = minecraft.Minecraft.create("localhost")
    return world

def set_minecraft_block():
    world = connect_to_mc()
    world.setBlock(0, 0, 0, 1)
  
def watch_for_key_press():
    raw_input() 
    set_minecraft_block()
    print("Manual overide is fully operationational")

if __name__ == "__main__":
    watch_for_key_press()

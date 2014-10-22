import ConfigParser
import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
from twilio.rest import TwilioRestClient

PHONE_CONFIG = {}

 
def load_twillio_config():

    config = ConfigParser.ConfigParser()
    config.read("api.config")
    PHONE_CONFIG["sid"] = config.get("phone", "sid")
    PHONE_CONFIG["to"] = config.get("phone", "to")
    PHONE_CONFIG["from"] = config.get("phone","from")
    PHONE_CONFIG["auth_token"] = config.get("phone", "auth_token")

def ring_phone():
    print("Calling phone")
    client = TwilioRestClient(PHONE_CONFIG["sid"], PHONE_CONFIG["auth_token"])
    call = client.calls.create(to=PHONE_CONFIG["to"],
		from_=PHONE_CONFIG["from"],
		url="http://twimlets.com/holdmusic",
		method="GET",
		fallback_method="GET",
		status_callback_method="GET",
		record="false")
    print(call.sid)

def changed_block(new_block_type):
    print("Changed. New block = " + str(new_block_type))
    ring_phone()


def monitor_block(world, block_location):
    [x,y,z] = block_location
    old_block_state = 0
    while True:
	new_block_state = world.getBlock(x, y, z)
	if new_block_state != old_block_state:
	    changed_block(new_block_state)
	    break
	sleep(0.1)

def connect():
    return minecraft.Minecraft.create("localhost", 4711)

if __name__ == "__main__":
    load_twillio_config()
    world = connect()
    print("conected to world")
    block_location = (3, 0.0, 0.0)
    monitor_block(world, block_location)



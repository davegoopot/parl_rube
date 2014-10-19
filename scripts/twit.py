from twitter import Twitter
import ConfigParser as configparser
from twitter import OAuth
from time import sleep
import mcpi.minecraft as minecraft



def auth():
    config = configparser.ConfigParser()
    config.read("api.config")
    auth_details = OAuth(config.get("api","token"),
        config.get("api", "token_secret"),
        config.get("api", "con_key"),
        config.get("api","con_secret"))



    return Twitter(auth=auth_details)



def find_max_id(query, t):
    results = t.search.tweets(q=query, result_type="recent")
    return results["search_metadata"]["max_id"]

def connect_to_mc():
    world = minecraft.Minecraft.create("localhost")
    return world

def set_minecraft_block():
    world = connect_to_mc()
    world.setBlock(0, 0, 0, 1)
  
def watch_for_tweet(query, t, max_id):
    while True:    
        results = t.search.tweets(q=query,
                                  since_id=max_id,
                                  result_type="recent")
        if results["statuses"]:
            print(results["statuses"][0]["text"])
            set_minecraft_block()
            break
        sleep(5)


if __name__ == "__main__":
    query = "python"
    t = auth()
    max_id = find_max_id(query, t)
    watch_for_tweet(query, t, max_id)
    print(max_id)

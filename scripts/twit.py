from twitter import Twitter
import ConfigParser as configparser
from twitter import OAuth
from time import sleep



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


  
def watch_for_tweet(query, t, max_id):
    while True:    
        results = t.search.tweets(q=query,
                                  since_id=max_id,
                                  result_type="recent")
        if results["statuses"]:
            print(results["statuses"][0]["text"])
            break
        sleep(5)


if __name__ == "__main__":
    query = "python"
    t = auth()
    max_id = find_max_id(query, t)
    watch_for_tweet(query, t, max_id)
    print(max_id)

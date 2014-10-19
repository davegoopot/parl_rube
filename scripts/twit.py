from twitter import Twitter
import ConfigParser as configparser
from twitter import OAuth



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
  


if __name__ == "__main__":
    query = "barney"
    t = auth()
    max_id = find_max_id(query, t)
    # watch_for_tweet(query, max_id)
    print(max_id)

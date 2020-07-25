from searchtweets import load_credentials
from searchtweets import collect_results
from searchtweets import gen_rule_payload

from textblob import TextBlob
import yaml
import pandas as pd
import re
import numpy as np
import tweepy
#from GUI import text

auth = tweepy.OAuthHandler('JUBWToPuyPfmzg8n117ZTllfB', 'lt0Psg46Nqzzaa4uel3wtSbaOyh9WiYIqx6ZH5xaExthndrsc1')
auth.set_access_token('1172272055183728640-nLQg9fvsLVieB9BXSsJq86a6kMmR8p', '5ogC7PXA1nmlNd5FCYtNaSIhF7tyA5K7CZzNBhi8qIhv1')

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")

except:
    print("Error during authentication")

config = dict(
    search_tweets_api = dict(
        account_type = 'premium',
        endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json',
        consumer_key = 'JUBWToPuyPfmzg8n117ZTllfB',
        consumer_secret = 'lt0Psg46Nqzzaa4uel3wtSbaOyh9WiYIqx6ZH5xaExthndrsc1'
    )
)

premium_search_args = load_credentials("twitter_keys_fullarchive.yaml",
                                       yaml_key="search_tweets_api",
                                       env_overwrite=False)


#query = "If this were green KSI"
query = "Benefits of having sites on Cloudflare"
rule = gen_rule_payload(query, from_date="2017-09-01", to_date="2020-07-19", results_per_call=100)
tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)

for tweet in tweets:
    print("text: %s" % tweet.text)
    print("number of likes: %d" % tweet.favorite_count)
    print("number of retweets: %d" % tweet.retweet_count)
    tw_obj = api.get_status(tweet.id)
    print("is a retweet: ", hasattr(tw_obj, 'retweeted_status'))






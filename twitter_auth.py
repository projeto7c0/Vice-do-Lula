import tweepy
import json

def authenticate():

    with open("config.json") as jsonfile:
        tt_config = json.load(jsonfile)['twitter-api']

        auth = tweepy.OAuthHandler(tt_config['consumer_token'], tt_config['consumer_secret'])
        auth.set_access_token(tt_config['key'], tt_config['secret'])

        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                        retry_errors=set([503]))

        return api
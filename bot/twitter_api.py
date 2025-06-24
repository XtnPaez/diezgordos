import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # carga variables desde .env si existiera

def create_client():
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_token, access_token_secret
    )
    client = tweepy.API(auth)
    return client

def tweet(status):
    client = create_client()
    client.update_status(status)

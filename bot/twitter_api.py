import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def create_client():
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    consumer_key = os.getenv("TWITTER_API_KEY")
    consumer_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    return client

def tweet(text):
    client = create_client()
    response = client.create_tweet(text=text)
    print("Tweet publicado, id:", response.data['id'])

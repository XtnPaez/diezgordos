import random
from twitter_api import create_api

def post_random_tweet(filename):
    api = create_api()
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    tweet = random.choice(lines)
    try:
        api.update_status(tweet)
        print(f"Tweet posteado: {tweet}")
    except Exception as e:
        print(f"Error posteando: {e}")

if __name__ == "__main__":
    post_random_tweet("data/frases.txt")

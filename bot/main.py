import os
import random
import tweepy

def post_random_tweet(file_path):
    bearer_token = os.getenv("BEARER_TOKEN")

    if not bearer_token:
        print("❌ Faltan las credenciales (BEARER_TOKEN)")
        return

    client = tweepy.Client(bearer_token=bearer_token)

    with open(file_path, 'r', encoding='utf-8') as f:
        frases = [line.strip() for line in f if line.strip()]

    tweet = random.choice(frases)

    try:
        response = client.create_tweet(text=tweet)
        print("✅ Tweet posteado:", tweet)
        print("🔗 Link:", f"https://twitter.com/user/status/{response.data['id']}")
    except Exception as e:
        print("❌ Error al postear:", e)

if __name__ == "__main__":
    post_random_tweet("data/frases.txt")

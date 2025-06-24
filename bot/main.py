import os
import random
import tweepy

def post_random_tweet(file_path):
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    if not all([api_key, api_secret, access_token, access_token_secret]):
        print("❌ Faltan credenciales.")
        return

    print("🔐 Credenciales cargadas. Creando cliente...")

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    print(f"📂 Leyendo archivo: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        frases = [line.strip() for line in f if line.strip()]

    print(f"📜 {len(frases)} frases encontradas.")
    if not frases:
        print("⚠️ No hay frases para twittear.")
        return

    tweet = "🐦 Esto es una prueba automática del bot #diezgordos"
    print(f"🎯 Frase elegida: {tweet}")

    try:
        response = client.create_tweet(text=tweet)
        tweet_id = response.data["id"]
        print(f"✅ Tweet posteado correctamente: https://twitter.com/i/web/status/{tweet_id}")
    except Exception as e:
        print("❌ Error al postear:", e)

if __name__ == "__main__":
    post_random_tweet("data/frases.txt")

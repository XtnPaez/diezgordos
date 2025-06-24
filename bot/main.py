from twitter_api import create_api

def post_tweet():
    api = create_api()
    tweet = "🐦 Esto es una prueba automática del bot #diezgordos"

    try:
        status = api.update_status(tweet)
        print(f"✅ Tweet posteado correctamente: https://twitter.com/i/web/status/{status.id}")
    except Exception as e:
        print("❌ Error al postear:", e)

if __name__ == "__main__":
    post_tweet()

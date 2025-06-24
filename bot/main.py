from twitter_api import create_api

def post_from_file(filename):
    api = create_api()
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = line.strip()
            if tweet:
                try:
                    api.update_status(tweet)
                    print(f"Tweet posteado: {tweet}")
                except Exception as e:
                    print(f"Error posteando: {e}")

if __name__ == "__main__":
    post_from_file("../data/frases.txt")

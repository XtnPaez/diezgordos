import random
from twitter_api import tweet

def main():
    with open("data/frases.txt", "r", encoding="utf-8") as f:
        frases = [line.strip() for line in f if line.strip()]
    if not frases:
        print("No hay frases para twittear.")
        return

    frase = random.choice(frases)
    tweet(frase)
    print(f"Tuiteado: {frase}")

if __name__ == "__main__":
    main()

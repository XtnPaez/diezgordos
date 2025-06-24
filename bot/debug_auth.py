import os

print("🕵️ Verificando variables de entorno...")

print("API_KEY:", os.getenv("API_KEY"))
print("API_SECRET:", os.getenv("API_SECRET"))
print("ACCESS_TOKEN:", os.getenv("ACCESS_TOKEN"))
print("ACCESS_TOKEN_SECRET:", os.getenv("ACCESS_TOKEN_SECRET"))

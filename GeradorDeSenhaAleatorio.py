import random
import string

caracteres = (
    string.ascii_letters + 
    string.ascii_uppercase +
    string.digits + 
    string.punctuation
)

senha = ''.join(random.choices(caracteres, k=14))
print("Gerando senha aleatória...")
print(f"Senha aleatória: {senha}")

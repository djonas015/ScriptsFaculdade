import random
print("Tente adivinhar o número entre 0 e 20")
num = random.randint(0, 20)

while True:
    n = int(input("Insira um número: "))
    if n == num:
        print("Parabéns! Você acertou.")
        break
    else:
        print("Tente novamente.")

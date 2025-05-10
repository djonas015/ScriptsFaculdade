import random
print("Tente adivinhar o número entre 0 e 100")
num = 0, 10
while True:
    random.randint(num)
    n = int(input("Insira um número: "))
    if n == num:
        print("Parabéns! Você acertou")
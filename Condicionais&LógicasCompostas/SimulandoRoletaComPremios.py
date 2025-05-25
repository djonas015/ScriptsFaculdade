import random

continuar = True
while continuar:
    inicio = input("Inicie a sorteio: ")
    premios = ['Nada', 'R$10', 'Camisa', 'Chaveiro', 'Vale-presente', 'R$100']
    sorteio = random.choice(premios)
    print(sorteio)
    continuar = input("Deseja rodar o sorteio novamente?: (s / n)")
    if continuar == 'n':
        print("Obrigado! volte quando quiser!")
        break

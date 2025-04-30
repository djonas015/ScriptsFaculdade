numero = int(input("Insira um número e receba sua tabuada: "))

for i in range(1, 11):
    tabuada = numero * i
    print(f"{numero} X {i} = {tabuada}")

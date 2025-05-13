base = int(input("Valor da base: "))
expoente = int(input("Valor do expoente: "))
resultado = 1
for i in range(expoente):
    resultado = base * resultado
print(resultado)

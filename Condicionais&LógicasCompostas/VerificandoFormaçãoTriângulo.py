ladoA = float(input("Lado A em cm: "))
ladoB = float(input("Lado B em cm: "))
ladoC = float(input("Lado C em cm: "))

if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")

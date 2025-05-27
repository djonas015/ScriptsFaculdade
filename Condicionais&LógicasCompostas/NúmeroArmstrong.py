num = int(input("Insira um número: "))
numstr = str(num)
soma = 0
for digito in numstr:
    soma += int(digito) ** len(numstr)
if soma == num:
    print(f"{numstr} é um número de armstrong")
else:
    print(f"{numstr} não é um número de armstrong")

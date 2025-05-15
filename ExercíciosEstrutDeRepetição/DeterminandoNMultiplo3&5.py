n = int(input("Insira um número: "))
if n % 3 == 0:
    print(f"{n} é multiplo de 3")
if n % 5 == 0:
    print(f"{n} é multiplo de 5")
if n % 3 != 0 and n % 5 != 0:
    print(f"{n} não é multiplo de 3 e 5")

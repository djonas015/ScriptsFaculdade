def multiplo():
    try:
        n1 = int(input("Insira um número: "))
        n2 = int(input("Insira outro numero: "))
        if n1 == 0:
            print("Erro! Não é possivel verificar por zero.")
            return
        if n2 % n1 == 0:
            print(f"{n2} é multiplo de {n1}")
        else:
            print(f"{n2} não é multiplo de {n1}")
    except ValueError:
        print("Por favor, insira apenas números inteiros.")


multiplo()

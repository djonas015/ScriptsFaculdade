def tabuada():
    n = int(input("Insira um número: "))
    for i in range(1, 11):
        resultado = i * n
        print(f"{n} X {i} = {resultado}")


tabuada()

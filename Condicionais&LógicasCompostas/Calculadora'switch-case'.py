n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

print("\n1. Soma(+)\n2. Subtração(-)\n3. Multiplicação(*)\n4. Divisão(/)")
operacao = input("\nEscolha a operação (+, -, *, /): ")
match operacao:
    case '+':
        resultado = n1 + n2
        print(f"Resultado: {resultado}")
    case '-':
        resultado = n1 - n2
        print(f"Resultado: {resultado}")
    case '*':
        resultado = n1 * n2
        print(f"Resultado: {resultado}")
    case '/':
        if n2 != 0:
            resultado = n1 / n2
            print(f"Resultado: {resultado}")
        else:
            print("Erro: divisão por zero!")
    case _:
        print("Operador inválido")

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))


def sinais(n1, n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Erro: divisão por zero."
    else:
        return "Erro: Operador inválido."


operador = input("Digite o operador(+, -, *, /): ")
calculo = sinais(n1, n2, operador)
print(f"O cálculo da sua conta é {calculo}")

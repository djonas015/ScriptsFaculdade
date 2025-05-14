continuar = 's'
while continuar == 's':
    operacao = input("Insira a operação matemática: "
                     "\n ( + ) ( - ) ( * ) ( / ) : ")
    if operacao == '+':
        n1 = float(input("1° número: "))
        n2 = float(input("2° número: "))
        resultado = n1 + n2
        print(f"{n1} + {n2} = {resultado}")
    if operacao == '-':
        n1 = float(input("1° número: "))
        n2 = float(input("2° número: "))
        resultado = n1 - n2
        print(f"{n1} - {n2} = {resultado}")
    if operacao == '*':
        n1 = float(input("1° número: "))
        n2 = float(input("2° número: "))
        resultado = n1 * n2
        print(f"{n1} * {n2} = {resultado}")
    if operacao == '/':
        n1 = float(input("1° número: "))
        n2 = float(input("2° número: "))
        if n2 == 0:
            print("Erro. Não é possivel dividir por 0")
        else:
            resultado = n1 / n2
            print(f"{n1} / {n2} = {resultado}")
    continuar = input("Deseja continuar o programa? (s / n)")
    if continuar == 'n':
        print("Programa encerrado. Até Logo")
        break

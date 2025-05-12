continuar = 's'
while continuar == 's':
    operacao = input("Selecione uma das operações abaixo:"
                     "\n( + ) ( - ) ( * ) ( / ) : ") 
    if operacao == '+':
        a = int(input("Insira 1° número: "))
        b = int(input("Insira 2° número: "))
        resultado = a + b
        print(f"{a} + {b} = {resultado}")         
    if operacao == '-':
        a = int(input("Insira 1° número: "))
        b = int(input("Insira 2° número: "))
        resultado = a - b
        print(f"{a} - {b} = {resultado}")
    if operacao == '*':
        a = int(input("Insira 1° número: "))
        b = int(input("Insira 2° número: "))
        resultado = a * b
        print(f"{a} * {b} = {resultado}")
    if operacao == '/':
        a = int(input("Insira 1° número: "))
        b = int(input("Insira 2° número: "))
        if b == 0:
            print("Erro. Não é possivel dividir por 0")
        else: 
            resultado = a / b
            print(f"{a} / {b} = {resultado}")
    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar == 'n':
        print("Obrigado por utilizar o programa. Até logo!")

def calculadora():
    print("Seja Bem vindo!")
    continuar = 's'
    while continuar:
        print("\n+\n-\n*\n/")
        opcao = input("\nSelecione a operação acima: ")
        match opcao:
            case '+':
                n1 = float(input("Insira o primeiro número: "))
                n2 = float(input("Insira o segundo número: "))
                resul = n1 + n2
                print(f"{n1} + {n2} = {resul}")
            case '-':
                n1 = float(input("Insira o primeiro número: "))
                n2 = float(input("Insira o segundo número: "))
                resul = n1 - n2
                print(f"{n1} - {n2} = {resul}")
            case '*':
                n1 = float(input("Insira o primeiro número: "))
                n2 = float(input("Insira o segundo número: "))
                resul = n1 * n2
                print(f"{n1} X {n2} = {resul}")
            case '/':
                n1 = float(input("Insira o primeiro número: "))
                n2 = float(input("Insira o segundo número: "))
                if n2 == 0:
                    print("Erro! Divisão por zero.")
                    return
                else:
                    resul = n1 / n2
                    print(f"{n1} / {n2} = {resul}")
        continuar = input("Deseja continuar no programa? (S / N): ").lower()
        if continuar == 'n':
            print("Obrigado por utilizar! Até logo.")
            break


calculadora()

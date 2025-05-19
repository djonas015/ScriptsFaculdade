caixa = 10500
print(f"Extrato Bancario: R${float(caixa):,.2f}")
while caixa > 0:
    opcao = input("Deseja: 1.Sacar / 2.Depositar : ")
    if opcao == '1':
        valorsaq = float(input("Insira o valor do saque: R$"))
        if valorsaq > caixa:
            print("Saldo indisponivel.")
        else:
            caixa -= valorsaq
            print(f"\nExtrato: \nR${caixa:,.2f}")
    elif opcao == '2':
        valordeposito = float(input("Insira o valor do depósito: R$"))
        caixa += valordeposito
        print(f"\nExtrato: \nR${caixa:,.2f}")
    else:
        print("Opção inválida.")
    atividade = input("Deseja Encerrar sua atividade? (S / N)").lower()
    if atividade == 's':
        break

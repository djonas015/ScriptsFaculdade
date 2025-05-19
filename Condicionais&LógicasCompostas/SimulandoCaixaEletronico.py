caixa = 10500
print(f"\nSaldo Bancario: R${float(caixa):,.2f}")
print('=' * 30)
while caixa > 0:
    opcao = input("Deseja: 1.Sacar / 2.Depositar : ")
    if opcao == '1':
        valorsaq = float(input("Insira o valor do saque: R$"))
        if valorsaq > caixa:
            print("Saldo indisponivel.")
        else:
            caixa -= valorsaq
            print(f"\nSaldo: \nR${caixa:,.2f}")
            print('=' * 30)
    elif opcao == '2':
        valordeposito = float(input("Insira o valor do depósito: R$"))
        caixa += valordeposito
        print(f"\nSaldo: \nR${caixa:,.2f}")
        print('=' * 30)
    else:
        print("Opção inválida.")
    atividade = input("Deseja Encerrar sua atividade? (S / N): ").lower()
    if atividade == 's':
        print("Sessão Encerrada. Obrigado! Até logo!")
        break

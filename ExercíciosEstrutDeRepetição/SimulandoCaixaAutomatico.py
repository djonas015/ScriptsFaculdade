saldo = int(input("Insira o saldo disponível: R$"))
for i in range(saldo):
    saque = int(input("Insira o valor desejavel para saque: R$"))
    if saque > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= saque
        print(f"Saldo disponível R${saldo}")
    if saldo == 0:
        print("Saldo indisponível")

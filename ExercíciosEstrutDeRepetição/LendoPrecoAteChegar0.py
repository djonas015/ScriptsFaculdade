pr1 = float(input("Insira o preço do produto: R$"))
while True:
    pr2 = float(input("Insira o preço do outro produto: R$"))
    if pr2 == 0:
        print("Valor R$0 digitado. Programa encerrado.")
        break
    else:
        pr1 += pr2
        print(f"Valor Total da Compra: R${pr1:,}")

divida = float(input("Valor da dívida: R$"))
while True:
    boletos = float(input("Insira o valor do boleto pago: R$"))
    divida -= boletos
    if divida > 0:
        print(f"restam R${divida:,} da dívida")
    else:
        print("Dívida paga.")
        break

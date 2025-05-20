real = float(input("Insira o valor que deseja converter: R$"))
opcoes = input("\n1.Dólar\n2.Euro\n3.Iene\n4.Libra\n5.Franco Suiço\nDigite Opção: ")
if opcoes == '1':
    dolar = real / 5
    print(f"U$D {dolar:.2f}")
elif opcoes == '2':
    euro = real / 5.40
    print(f"EUR €{euro:.2f}")
elif opcoes == '3':
    iene = real * 28
    print(f"JPY ¥{iene:.2f}")
elif opcoes == '4':
    libra = real / 6.30
    print(f"GBR £{libra:.2f}")
elif opcoes == '5':
    franco = real / 5.50
    print(f"CHF Fr.{franco:.2f}")
else:
    print("Opção inválida")

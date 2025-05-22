print("\nBem-Vindo a Pizzaria Bela Pizza!")
print("\nDeseja:\n1.Escolher sabor pronto\n2.Monte do seu jeito")
print('=' * 30)
sabores = input("Digite a opção: ")
if sabores == '1':
    print("1.Mussarela\n2.Calabresa\n3.Frango com Catupiry\n4.Quatro Queijos\n5.Chocolate com Morango\n")
    sbr = input("Digite a opção: ")
    print('=' * 30)
    match sbr:
        case '1':
            print("Pizza 1.Mussarela selecionada")
            print("Preço: R$45,90")
        case '2':
            print("Pizza 2.Calabresa selecionada")
            print("Preço: R$42,90")
        case '3':
            print("Pizza 3.Frango com Catupiry selecionada")
            print("Preço: R$47,50")
        case '4':
            print("Pizza 4.Quatro Queijos selecionada")
            print("Preço: R$48,90")
        case '5':
            print("Pizza 5.Chocolate com Morango selecionada")
            print("Preço: R$46,50")
        case _:
            print("Operação inválida")
elif sabores == '2':
    print("\nSelecione o ingrediente:")
    print("\n1.Mussarela\n2.Calabresa\n3.Frango desfiado\n4.Catupiry\n5.Bacon\n6.Milho\n7.Gorgonzola")
    print('=' * 30)
    sbr2 = input("Digite a opção: ")
    ingredientes = {
        '1': ('Musarela', 5.00),
        '2': ('Calabresa', 6.00),
        '3': ('Frango desfiado', 7.00),
        '4': ('Catupiry', 6.50),
        '5': ('Bacon', 6.50),
        '6': ('Milho', 3.00),
        '7': ('Gorgonzola', 7.50)
    }
    escolhas = sbr2.split(',')
    precoinicial = 30.00
    total = precoinicial
    print("\nIngredientes selecionados: ")
    for item in escolhas:
        ingr = ingredientes.get(item.strip())
        if ingr:
            print(f"{ingr[0]} (+R${ingr[1]:.2f})")
            total += ingr[1]
        else:
            print("Ingrediente inválido")
    print(f"\nPreço final da pizza R${total:.2f}")
else:
    print("Opção inválida")

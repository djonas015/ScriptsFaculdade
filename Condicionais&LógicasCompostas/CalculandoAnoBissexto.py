ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        print(f"{ano} é bissexto")
    elif ano % 400 == 0:
        print(f"{ano} é bissexto")
    else:
        print(f"{ano} não é bissexto")
else:
    print(f"{ano} não é bissexto")

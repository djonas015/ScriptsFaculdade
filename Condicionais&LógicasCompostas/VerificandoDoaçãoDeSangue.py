idade = int(input("Idade: "))
peso = float(input("Peso: "))
saude = input("Está Bem de saúde? (s / n)")
alimentacao = input("Está bem alimentado? (s / n)")
documento = input("Está com documento com foto? (s / n)")

if idade >= 16 and idade <= 69:
    if peso >= 50:
        if saude == 's':
            if alimentacao == 's':
                if documento == 's':
                    print("Pode Doar Sangue!")
                else:
                    print("Não Pode Doar Sangue!")
            else:
                print("Não Pode Doar Sangue!")
        else:
            print("Não Pode Doar Sangue!")
else:
    print("Não pode doar sangue")

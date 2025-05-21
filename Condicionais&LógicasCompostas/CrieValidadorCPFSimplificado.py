cpf = input("Insira o CPF: ")
formatacao = ''.join(filter(str.isdigit, cpf))
if len(formatacao) == 11:
    if all(digito == formatacao[0] for digito in formatacao):
        print("CPF inválido: todos os dígitos são iguais.")
        exit()
    else:
        cpf_digitos = formatacao[:9]
        peso = 10
        soma = 0
        for digitos in cpf_digitos:
            num = int(digitos)
            soma += num * peso
            peso -= 1
        resultado = (soma * 10) % 11
        if resultado >= 10:
            verif1 = 0
        else:
            verif1 = resultado  
        cpf_digitos += str(verif1)
        peso = 11
        soma = 0
        for digitos in cpf_digitos:
            num = int(digitos)
            soma += num * peso
            peso -= 1
        resultado = (soma * 10) % 11
        if resultado == 10:
            verif2 = 0
        else:
            verif2 = resultado         
        if int(formatacao[9]) == verif1 and int(formatacao[10]) == verif2:
            print("CPF válido!")
        else:
            print("CPF inválido")
else:
    print("CPF inválido: deve conter exatamente 11 dígitos.")

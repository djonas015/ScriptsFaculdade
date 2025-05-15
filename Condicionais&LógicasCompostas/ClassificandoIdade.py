idade = int(input("Insira a idade: "))
if idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 64:
    print("adulto")
else:
    print("idoso")

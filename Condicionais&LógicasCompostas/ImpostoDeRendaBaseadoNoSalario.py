salario = float(input("Insira a renda mensal: R$"))
if salario <= 2260:
    print("Isento")
elif salario <= 2826:
    print("7,5% alíquota")
elif salario <= 3751:
    print("15% alíquota")
elif salario <= 4664:
    print("22,5% alíquota")
else:
    print("27,5% alíquota")

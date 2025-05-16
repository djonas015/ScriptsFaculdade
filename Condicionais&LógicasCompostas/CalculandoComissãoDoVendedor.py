v1 = input("Valor da venda: R$")
v1 = v1.replace('.', '').replace(',', '.')
venda = float(v1)
if venda <= 1000:
    print("5% de comissão")
elif venda <= 5000:
    print("10% de comissão")
else:
    print("15% de Comissão")

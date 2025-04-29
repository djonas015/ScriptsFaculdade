precoantigo = float(input("Preço antigo: R$"))
preconovo = float(input("Novo preço: R$"))
aumentopercent = ((precoantigo - preconovo) / precoantigo) * -100
print(f"O produto teve um aumento percentual de {aumentopercent:.2f}%")

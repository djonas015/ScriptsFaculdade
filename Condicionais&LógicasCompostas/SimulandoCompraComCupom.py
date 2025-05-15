produto = float(input("Insira o preço do produto R$"))
cupom = int(input("Insira o cupom %"))
prodfinal = produto - (produto * (cupom / 100))
print(f"Produto com desconto final R${prodfinal:,}")

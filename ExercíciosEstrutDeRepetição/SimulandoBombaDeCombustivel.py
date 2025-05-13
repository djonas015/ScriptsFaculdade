import time

tanque = float(input("Limite do tanque em litos: "))
combustivel = float(input("Combustível no tanque em litros: "))
tanquetotal = tanque - combustivel
print(f"O tanque possui {tanquetotal} litros de espaço.")
comb = float(input("Deseja colocar quantos litros no tanque?: "))
litros = 0
if comb > tanquetotal:
    print(f"Não é possível colocar {comb}L. Só cabem {tanquetotal}L")
else:
    litros = 0
    print("Abastecendo...")
    while litros < comb:
        litros += 1
        print(f"{litros:02}L")
        time.sleep(0.2)
        if litros == comb:
            break
    print("Abastecimento concluído. Volte sempre!")

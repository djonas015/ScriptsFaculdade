n1 = []

print("Insira 7 números inteiros, depois solicite qualquer número. \n"
      "Verificaremos se o número se encontra no array.")

for i in range(7):
    num = int(input(f"Insira o {i + 1}° número inteiro: "))
    n1.append(num)

num_extra = int(input("Insira um número para sua verificação."))
verific = num_extra in n1
if verific == True:
    print(f"O número {num_extra} foi localizado no array!")
else:
    print(f"O número {num_extra} não foi encontrado no array.")

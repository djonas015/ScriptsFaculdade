cand1 = 'João - 45'
cand2 = 'Marcos - 61'
cand3 = 'Felipe - 37'
votoc1 = 0
votoc2 = 0
votoc3 = 0
print("Candidatos da votação e seus respectivos números" 
      f"\n{cand1}\n{cand2}\n{cand3}")
while True:
    voto = input("Insira o número do candidato: ")
    if voto == '45':
        votoc1 += 1
    if voto == '61':
        votoc2 += 1
    if voto == '37':
        votoc3 += 1
    resposta = input("Obrigado pelo voto! Deseja continuar? (s/n)")
    if resposta == 'n':
        rsfinal = [
            ("João - 45", votoc1),
            ("Marcos - 61", votoc2),
            ("Felipe - 37", votoc3)
        ]
        resultado = max(rsfinal, key=lambda x: x[1])
        print(f"O candidato mais votado foi {resultado}")
        break

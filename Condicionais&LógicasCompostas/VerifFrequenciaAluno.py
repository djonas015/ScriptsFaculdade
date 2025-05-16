aulas = int(input("Número de aulas: "))
frequencia = int(input("Número de aulas que o aluno compareceu: "))
calculo = (frequencia / aulas) * 100
if calculo >= 75:
    print(f"Aluno Aprovado. Frequência do aluno: {calculo:.02f}%")
else:
    print(f"Aluno Reprovado. Frequencia do aluno: {calculo:.2f}%")

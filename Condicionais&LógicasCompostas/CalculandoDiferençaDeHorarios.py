print("Insira o primeiro horário")
h1 = int(input("Horas: "))
m1 = int(input("Minutos: "))
s1 = int(input("Segundos: "))
print(f"{h1:02}:{m1:02}:{s1:02}")
timer1 = s1 + (h1 * 3600) + (m1 * 60)
print("\nInsira o segundo horario")
h2 = int(input("Horas: "))
m2 = int(input("Minutos: "))
s2 = int(input("Segundos: "))
print(f"{h2:02}:{m2:02}:{s2:02}")
timer2 = s2 + (h2 * 3600) + (m2 * 60)
diferenca = timer1 - timer2
diferencahoras = diferenca // 3600
diferencaminutos = (diferenca % 3600) // 60
diferencasegs = diferenca % 60
print("\nDiferença entre horários:")
print(f"{diferencahoras:02}:{diferencaminutos:02}:{diferencasegs:02}")

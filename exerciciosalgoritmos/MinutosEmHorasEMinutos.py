minutos = int(input("Insira os minutos: "))
horas = minutos // 60
minutosrestantes = minutos % 60
if minutosrestantes == 0:
    print(f"{horas} hora(s)")
else:
    print(f"{horas} hora(s) e {minutosrestantes} minuto(s)")

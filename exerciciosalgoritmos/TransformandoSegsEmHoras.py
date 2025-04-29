segundos = int(input("Insira os segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) / 60
if horas == 0:
    print(f"{minutos:.0f} minuto(s)")
else:
    print(f"{horas:.0f} hora(s) e {minutos:.0f} minuto(s)")

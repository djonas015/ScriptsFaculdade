import time

segundos = 0
minutos = 0
horas = 0
while True:
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)
    segundos += 1
    if segundos == 59:
        segundos = 0
        minutos += 1
        if minutos == 59:
            minutos = 0
            horas += 1
            if horas == 24:
                break
    if horas == 24:
        break

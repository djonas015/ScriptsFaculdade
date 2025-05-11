import time

seg = int(input("Deseja marcar quantos segundos?: "))
min = int(input("Quantos minutos?: "))
horas = int(input("Quantas horas?: "))
timer = seg + (min * 60) + (horas * 3600)
while timer > 0:
    h = timer // 3600
    minutos = (timer % 3600) // 60
    segnds = timer % 60
    print(f"{h:02}:{minutos:02}:{segnds:02}") 
    time.sleep(0.08)
    timer -= 1

print('Timer encerrado')

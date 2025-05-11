import time

seg = 0
min = 0
horas = 0
while True:
    print(f"{horas}:{min}:{seg}")
    time.sleep(1)
    seg += 1
    if seg == 60:
        seg = 0
        min += 1
        if min == 60:
            min = 0
            horas += 1
            if horas == 24:
                break
    if horas == 24:
        break

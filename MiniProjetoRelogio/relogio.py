import time

seg = 0
mins = 0
horas = 0
print("RELÓGIO:")
while True:
    print(f"{horas:02}:{mins:02}:{seg:02}")
    time.sleep(1)
    seg += 1
    if seg == 60:
        seg = 0
        mins += 1
        if mins == 60:
            mins = 0
            horas += 1
            if horas == 24:
                break
    if horas == 24:
        break

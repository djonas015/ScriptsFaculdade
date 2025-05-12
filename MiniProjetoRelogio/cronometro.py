import time
import keyboard

seg = 0
min = 0
hrs = 0

print("Inície o cronomêtro")
input("Pressione Enter para começar o cronomêtro...")
print("Pressione a tecla 'P' para encerrar o programa")

while True:
    print(f"{hrs:02}:{min:02}:{seg:02}")
    time.sleep(1)
    seg += 1
    if seg == 60:
        seg = 0
        min += 1
        if min == 60:
            min = 0
            hrs += 1
            if hrs == 24:
                break
    if keyboard.is_pressed("P"):
        print("Programa Encerrado!")
        break

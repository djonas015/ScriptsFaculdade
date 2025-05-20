import pygame
import time

pygame.init()
pygame.mixer.init() 

seg = int(input("Segundos: "))
mits = int(input("Minutos: "))
horas = int(input("Horas: "))
alarme = seg + (mits * 60) + (horas * 3600) 
while alarme > 0:
    hs = alarme // 3600
    minutos = (alarme % 3600) // 60
    sgs = alarme % 60
    print(f"{hs:02}:{minutos:02}:{sgs:02}")
    time.sleep(1)
    alarme -= 1
pygame.mixer.music.load('C:/Users/diasj/OneDrive/Desktop/Estudos/ScriptsFaculdade/Condicionais&LógicasCompostas/audio.mp3')
pygame.mixer.music.play()
print("Alarme!")
while pygame.mixer.music.get_busy():
    time.sleep(0.1)

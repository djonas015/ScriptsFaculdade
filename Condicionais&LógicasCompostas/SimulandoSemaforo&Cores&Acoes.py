import time
from colorama import Fore, init
init()
semaforo = 0
while True:
    print(f"{semaforo:02}")
    if semaforo == 0:
        print(Fore.GREEN + "VERDE - SIGA")
    if semaforo == 30:
        print(Fore.YELLOW + "ATENÇÃO - AMARELO")
    if semaforo == 40:
        print(Fore.RED + "PARE - VERMELHO")
    elif semaforo == 60:
        semaforo = -1

    time.sleep(0.5)
    semaforo += 1

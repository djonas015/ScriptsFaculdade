import time

tempideal = float(input("Insira a temperatura ideal do forno em °C:"))
tempinicial = 0
while tempinicial < tempideal:
    print(f"{tempinicial}°C")
    time.sleep(0.1)
    tempinicial += 1
    if tempinicial == tempideal:
        print(f"forno está na temperatura de {tempideal}°C")

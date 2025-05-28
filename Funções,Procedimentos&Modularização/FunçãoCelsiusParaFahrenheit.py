def graus():
    celsius = float(input("Insira a temperatura em celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


print(f"Temperatura em fahrenheit: {graus()}")

def area_circulo():
    raio = float(input("Insira o raio do círculo: "))
    area = 3.1416 * (raio ** 2)
    return area


print(f"Área do círculo: {area_circulo():.2f}cm²")

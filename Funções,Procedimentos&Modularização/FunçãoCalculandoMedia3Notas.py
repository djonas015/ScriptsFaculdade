def media():
    resultado = 0
    for i in range(3):
        n = int(input(f"Insira o {i + 1}° número: "))
        resultado += n
        media = resultado / 3
    return media


print(f"{media()}")

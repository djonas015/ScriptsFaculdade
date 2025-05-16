palavra = input("Insira uma palavra: ")
if palavra.lower().count("admin"):
    print("A palavra possui 'admin' em sua composição")
else:
    print("A palavra não possui 'admin' em sua composição")

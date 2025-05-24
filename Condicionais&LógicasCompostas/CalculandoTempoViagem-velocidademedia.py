distancia = float(input("Insira a distancia em km: "))
velocidade = float(input("Insira a velocidade média km/h: "))
tempo = distancia / velocidade
horas = int(tempo)
minutos = (tempo - horas) * 60
minutos = distancia % velocidade
print(f"{horas:.2f} horas e {minutos:.2f} minutos")

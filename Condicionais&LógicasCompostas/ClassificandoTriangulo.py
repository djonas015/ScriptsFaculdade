l1 = float(input("Primeiro lado: "))
l2 = float(input("Segundo lado: "))
l3 = float(input("Terceiro lado: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print("Equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isósceles")
    else:
        print("Escaleno")

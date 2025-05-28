primo = int(input("Insira um número: "))


def verif(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


if verif(primo):
    print(f"O número {primo} é primo")
else:
    print(f"O número {primo} não é primo")

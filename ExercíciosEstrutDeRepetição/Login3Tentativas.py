login = 'user@2025'
senha = '2025'
print("\nVocê possui 3 tentaivas de login")
for i in range(3):
    lguser = input("Login:")
    shuser = input("Senha:")
    if (lguser, shuser) == (login, senha):
        print("Login e Senha correto. Acesse o sistema")
        break
    else:
        print("Login ou Senha incorretos.")

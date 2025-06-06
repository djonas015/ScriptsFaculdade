def algoritmo_senha():
    user_original = 'user2025'
    senha_original = '2025@'
    tentativas = 0
    while tentativas < 3:
        user_terminal = input("User: ")
        senha_terminal = input("Senha: ")
        if user_terminal == user_original and senha_terminal == senha_original:
            print("Acesso liberado")
            break
        else:
            print("Acesso negado")
            tentativas += 1
        if tentativas == 3:
            print("Número máximo de tentativas atingido.")


algoritmo_senha()

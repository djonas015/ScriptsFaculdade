import sqlite3

conn = sqlite3.connect("agenda.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT
)
""")


conn.commit()


def add_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    cursor.execute("INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    print("Contato adicionado com sucesso! \n")


def menu():
    while True:
        print("=== AGENDA DE CONTATOS ===")
        print("1. Adicionar contato")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")      
        if opcao == "1":
            add_contato()
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente. \n")


menu()

conn.close()

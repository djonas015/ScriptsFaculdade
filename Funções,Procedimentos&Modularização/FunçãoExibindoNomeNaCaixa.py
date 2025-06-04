def caixa():
    n = input("Insira seu nome: ")
    largura = max(20, len(n) + 4)
    print('_' * largura)
    print('|' + n.center(largura - 2) + '|')
    print('‾' * largura)


caixa()

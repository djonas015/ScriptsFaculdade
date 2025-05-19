caixa = 3000  # saldo da conta
print(caixa)  # imprimindo saldo
notas = [100, 50, 20, 10, 2, 5]  # lista com o valor das notas em ordem
while caixa > 0:  # bloco de repetição. repetir ate chegar em 0
    saque = float(input("v. saque: "))  # user insere valor de saque
    if saque > caixa:  # Se valor de saque for maior do que saldo na conta
        print("o. invalida")  # imprime isso
    else:  # senao
        resto = int(saque)  # cria nova variavel e tranforma saque(float) em int
        notausada = {}  # cria nova variavel para armazenar as notas que forem usar
               
        for nota in notas:  # (cria nova variavel 'nota') / ver nota em notas
            qtd = resto // nota  # cria nova variavel e faz divisão completa entre resto(que era saque) por nota, variavel criada agr
            if qtd > 0:  # se qtd for maior que 0
                notausada[nota] = qtd  # armazena as notas que estão sendo usadas no saque
                resto %= nota  # resto calcula o resto da divisão de (notas)
        if resto != 0:  # se resto for diferente de zero
            print('Erro')  # imprime isso
        else:  # senao
            for nota, qtd in notausada.items():  # percorrer o dicionário (notausada) e imprime cada par de chave e valor
                print(f"{qtd} nota(s) de R${nota}")  # imprime isso
                caixa -= saque  # aqui caixa(ou saldo da conta) subtrai o valor do saque e ja atualiza.

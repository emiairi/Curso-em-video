# Desafio 104 - Validando entrada de dados em Python

'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só
que fazendo a validação para aceitar apenas um valor numérico.
Ex.:
n=leiaInt(Digite um n)'''


def leiaInt(mensagem):
    m = input(mensagem)
    while not m.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        m = input(mensagem)
    return m

'''Solução Guanabara:
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
            '''
n=leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
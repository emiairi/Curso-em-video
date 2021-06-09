# Desafio 059 - Criando um Menu de Opções

'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

menu = '''Escolha uma das opçoes:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa'''
opcao = 0

while opcao != 5:
    print(menu)
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('{} + {} = {}' .format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'. format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}.' .format(n1, n2))
        else:
            print('{} é maior que {}.' .format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    sleep(2)
print('Fim do Programa!!!')
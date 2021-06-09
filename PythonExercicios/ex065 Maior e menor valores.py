# Desafio 065 - Maior e Menos Valores

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''

quant = 0
soma = 0
op = 'S'

while op in 'sS':
    n = int(input('Digite um número: '))
    if quant == 0:
        maior = n
        menor = n
    soma += n
    quant += 1
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    while op != 'N' and op != 'S':
        print('Opção inválida. Tente novamente.')
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

print('A soma foi {}'.format(soma))
print('Quantidade {}'.format(quant))
print('Média {:.2f}'.format(soma/quant))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))

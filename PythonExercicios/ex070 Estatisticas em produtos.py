# Desafio 070 - Estatísticas em produtos

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.'''

print('-' * 30)
print('{: ^}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

total = mais = 0
prodbarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    if total == 0:
        barato = preco
        prodbarato = produto

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida. Tente novamente.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    # Total de gastos com a compra
    total += preco

    # Produtos que custam mais que R$ 1000
    if preco > 1000:
        mais += 1

    # Produto mais barato
    if preco <= barato:
        barato = preco
        prodbarato = produto

    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mais} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prodbarato.upper()} que custa R$ {barato:.2f}')


# Desafio 084 - Lista composta e análise de dados

'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''
pessoa = list()
temp = list()
pesado = leve = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        pesado = leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    pessoa.append(temp[:])
    temp.clear()

    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    while cont not in 'SN' or cont in ' ':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont in 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoa)} pessoas.')
print(f'O maior peso foi de {pesado:.1f}Kg. Peso de ', end='')
for c in pessoa:
    if c[1] == pesado:
        print(f'[{c[0]}]', end=' ')

print(f'\nO menor peso foi de {leve:.1f}Kg. Peso de ', end='')
for l in pessoa:
    if l[1] == leve:
        print(f'[{l[0]}]', end=' ')




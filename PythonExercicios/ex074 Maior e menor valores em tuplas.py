# Desafio 074 - Maior e menor valores em Tupla

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

maior = menor = 0

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteado foram', end=' ')

for valores in tupla:
    print(valores, end=' ')

print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')

for n in range(0, len(tupla)):
    if n == 0:
        maior = tupla[n]
        menor = tupla[n]
    else:
        if tupla[n] > maior:
            maior = tupla[n]
        if tupla[n] < menor:
            menor = tupla[n]
print(f'\nO maior valor sorteado foi com for {maior}')
print(f'O menor valor sorteado foi com for {menor}')
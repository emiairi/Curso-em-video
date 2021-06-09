# Desafio 078 - Maior e Menor valores na Lista

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = list()
maior = menor = 0

for posição in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posição {posição}: ')))
    if posição == 0:
        maior = menor = lista[0]
    else:
        if lista[posição] > maior:
            maior = lista[posição]
        if lista[posição] < menor:
            menor = lista[posição]

print('=-' * 25)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, val in enumerate(lista):
    if maior == val:
        print(f'{pos}', end='...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, val in enumerate(lista):
    if menor == val:
        print(f'{pos}', end='...')
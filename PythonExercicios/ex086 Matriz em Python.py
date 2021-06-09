# Desafio 086 - Matriz em Python

'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

for m in range(0, 3):
    for n in range(0, 3):
        print(f'[ {matriz[m][n]:^5} ]', end='')
    print()


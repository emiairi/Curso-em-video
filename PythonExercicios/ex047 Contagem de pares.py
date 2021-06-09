# Desafio 047 - Contagem de pares

'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('Os números pares no intervalo de 1 até 50 são: ')

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')

print('\n')
for n in range(2, 51, 2):
    print(n,end=' ')
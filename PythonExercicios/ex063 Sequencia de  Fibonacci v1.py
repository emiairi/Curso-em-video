# Desafio 063 - Sequência de Fibonacci v1.0

'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma SequÊncia
de Fibonacci.
Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8...'''

n = int(input('Números de elementos da Sequência Fibonacci: '))
cont = 3
anterior = 0
atual = 1
soma = 0
print('{} -> {}'.format(anterior, atual), end='')

while cont <= n:
    soma = anterior + atual
    print(' -> {}'.format(soma), end='')
    anterior = atual
    atual = soma
    cont += 1

print(' -> \033[1;31mFIM\033[m')
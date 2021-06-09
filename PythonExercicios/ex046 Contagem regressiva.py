# Desafio 046 - Contagem regressiva

'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('\033[1;31mB\033[m'+'\033[1;33mU\033[m'+'\033[1;34mM\033[m'+'\033[1;35mM\033[m'+'\033[1;36mM\033[m')

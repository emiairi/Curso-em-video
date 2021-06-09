# Desafio 100 - Funções para sortear e somar

'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores PARES sorteados pela função anterior.'''

from random import randint
from time import sleep


def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        s = randint(1, 10)
        numeros.append(s)
        sleep(0.5)
        print(s, end=' ')
    print('PRONTO!')
    somaPar(numeros)


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteio()
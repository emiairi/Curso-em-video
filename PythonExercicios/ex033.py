# Desafio 033 - Maior e menos valores.

"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite o último número inteiro: '))

lista = [n1, n2, n3]

print('Menor: {} / Maior: {}' .format(min(lista), max(lista)))

lista.sort()

print('O maior número é: {}, e o menor número é: {}' .format(lista[2], lista[0]))
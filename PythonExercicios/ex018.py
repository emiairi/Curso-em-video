# Desafio 018
"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

import math

ang = float(input('Digite o valor do ângulo: '))

angrad = math.radians(ang)

print('O valor do seno do ângulo {} é {:.2f}.'.format(ang, math.sin(angrad)))
print('O valor do cosseno do ângulo {} é {:.2f}.'.format(ang, math.cos(angrad)))
print('O valor da tangente do ângulo {} é {:.2f}.'.format(ang, math.tan(angrad)))

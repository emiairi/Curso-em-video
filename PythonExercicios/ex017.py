# Desafio 017
"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa."""
import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa do co {} e do ca {} é {}.'.format(co, ca, math.hypot(co, ca)))

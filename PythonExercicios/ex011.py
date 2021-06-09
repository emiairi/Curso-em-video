# Desafio 011
"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
   de tinta necessária para pintá-la, sabendo que cada  litro de tinta pinta uma área de 2m2."""

l = float(input('Qual a largura da parede em metros? '))
h = float(input('Qual a altura da parede em metros? '))
a = l * h
t = a / 2

print('A área é de: {}m²'.format(a))
print('Será utilizado {} l de tinta.'.format(t))

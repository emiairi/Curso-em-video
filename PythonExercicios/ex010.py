# Desafio 010
"""Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$ 1,00 = R$ 3,27"""

d = float(input('Qual o valor que tem na carteira? R$ '))
c = d / 3.27
print('US$ {:.2f}'.format(c))
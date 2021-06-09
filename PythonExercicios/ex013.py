# Desafio 013
"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

s = float(input('Qual o valor do seu salário? R$ '))
a = s + (s * 0.15)

print('O seu novo salário será de R$ {:.2f}'.format(a))
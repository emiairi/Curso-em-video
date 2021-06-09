# Deafio 031 - Custo da Viagem.

"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagem até 200 km e R$ 0,45 para viagem mais longa."""

dist = float(input('Distância da viagem? '))

if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45

print('O valor da viagem será: R$ {:.2f}'.format(valor))
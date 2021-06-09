# Desafio 014

"""Escreva um programa que converta uma temperatura digitada em °C para °F."""

c = float(input('Informe a temperatura em °C: '))
f = 1.8 * c + 32
print('A temperatura de {:.1f}°C corresponde a {}°F'.format(c, f))
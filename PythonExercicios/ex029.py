# Desafio 029 - Radar eletrônico.

"""Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$ 7,00 por cada kh acima do limite."""

lim = 80

vel = float(input('Qual a velocidade do carro em km/h? '))

if vel > lim:
    multa = 7 * (vel - lim)
    print('Você foi multado em: R$ {:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
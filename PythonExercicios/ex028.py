# Desafio 028 - Jogo da adivinhação v 1.0

""" Escreva um programa  que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
tentar adivinhar qual foi o número escolhido pelo computador.
    O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

computador = randint(0, 5)

num = int(input('Em que número pensei? '))

print('PROCESSANDO...')
sleep(3)

if num == computador:
    print('PARABÉNS! Você conseguiu adivinhar!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!' .format(computador, num))



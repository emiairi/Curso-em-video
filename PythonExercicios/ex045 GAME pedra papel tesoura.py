# Desafio 045 - GAME: Pedra, papel e tesoura.

"""Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint

print('=-' * 15)
print(' ' * 9, 'JOKENPÔ')
print('=-' * 15)

itens = ('PEDRA', 'PAPEL', 'TESOURA')

print('''Escolha a sua jogada:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogada = int(input('Jogada: '))

computador = randint(0, 2)

print('Computador jogou {}.' .format(itens[computador]))
print('Você jogou {}.' .format(itens[jogada]))

venceu = '\033[1;36mPARABÉNS!!! VOCÊ VENCEU!!!\033[m'
perdeu = '\033[1;31mVocê perdeu!!!\033[m'

if jogada == computador:
    print('\033[1;33mEMPATE\033[m')
elif jogada == 0:
    if computador == 1:
        print(perdeu)
    elif computador == 2:
        print(venceu)
elif jogada == 1:
    if computador == 0:
        print(venceu)
    elif computador == 2:
        print(perdeu)
elif jogada == 2:
    if computador == 0:
        print(perdeu)
    elif computador == 1:
        print(venceu)
else:
    print('Opção inválida')

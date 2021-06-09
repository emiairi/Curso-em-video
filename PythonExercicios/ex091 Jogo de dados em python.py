# Desafio 091 - Jogo de Dados em Python

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print('Valores sorteados:')
print(jogadores)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)

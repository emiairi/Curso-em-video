# Desafio 106 - Sistema interativo de ajuda em Python

'''Faça um mini-sistema que utilize o interactive Hel do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavre FIM, o programa se encerrará.'''

from time import sleep
cores = {'azul': '\033[1;30;44m',
         'vermelho': '\033[1;30;41m',
         'verde': '\033[1;30;42m',
         'branco': '\033[7;30m'
         }


def ajuda(com):
    titulo('azul', f'Acessando o manual do comando \'{com}\'')
    print(cores['branco'])
    help(com)
    print('\033[m', end='')
    sleep(2)


def titulo(cor, msg):
    tam = len(msg) + 4
    print(f'{cores[cor]}~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m', end='')
    sleep(1)


while True:
    titulo('verde', 'SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)

titulo('vermelho', 'ATÉ LOGO!')
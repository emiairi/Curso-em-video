# Desafio 088 - Palpites para a Mega Sena

'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
jogadas = []
temp = []
print('-' * 30)
print('      JOGADA MEGA SENA      ')
print('-' * 30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 3, f'SORTEANDO {jogos} JOGOS', '-=' * 3)
s = 1
for j in range(0, jogos):
    while s < 7:
        sorteio = randint(1, 60)
        if sorteio not in temp:
            temp.append(sorteio)
            s += 1
    temp.sort()
    jogadas.append(temp[:])
    s = 1
    temp.clear()
for c in range(0, jogos):
    print(f'Jogo {c+1}: {jogadas[c]}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

# Solução Guanabara ---
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
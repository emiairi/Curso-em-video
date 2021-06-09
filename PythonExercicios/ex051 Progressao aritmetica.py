# Desafio 051 - Pregressão Aritmética

'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão.'''

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print(c, end=' ')
    #p += r

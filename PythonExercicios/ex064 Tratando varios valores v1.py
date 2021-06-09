# Desafio 064 - Tratando vários valores v1.0

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

parada = 999
n = int(input('Digite um número [999 para parar]: '))
quantidade = 0
soma = 0

while n != parada:
    quantidade += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma deles foi {}.' .format(quantidade, soma))

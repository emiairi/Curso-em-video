# Desafio 054 - Grupo da Maioridade

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.'''

from datetime import date

anoAtual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input('Ano de nascimento: '))
    idade = anoAtual - ano
    print('Idade: {}.' .format(idade))
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoas já atingiram a maioridade.' .format(maior))
print('{} pessoas não atingiram a maioridade.' .format(menor))

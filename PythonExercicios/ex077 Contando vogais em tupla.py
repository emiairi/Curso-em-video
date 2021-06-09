# Desafio 077 - Contando vogais em Tupla

'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for c in palavras:
    print(f'\nNa palavra {c} temos', end=' ')
    for vogal in c:
        if vogal.upper() in 'AEIOU':
            print(vogal, end=' ')



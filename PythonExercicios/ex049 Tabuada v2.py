# Desafio 049 - Tabuada v2.0

'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Qual tabuada quer aprender: '))
l = int(input('Qual o limite da tabuada: '))

for c in range(1, l + 1):
    print('{} x {:2} = {}' .format(n, c, n * c))

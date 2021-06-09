# Desafio 042 - Analisando Triângulos v2.0

"""Refaça o DESAFIO 035 dos triângulos, ascrescentando o recurso de mostrar que tipo de triângulo será formado:
    -> Equilátero: todos os lados iguais
    -> Isósceles: dois lados iguais
    -> Escaleno: todos os lados diferentes."""

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

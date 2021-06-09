# Desafio 008
'''Escreva um programa que leia um valor em metros e o exiba convertido em contímetros e milímetros'''

n = float(input('Digite o valor em metros: '))

cm = n * 100
mm = n * 1000

print('{}m >>> {}cm >>> {}mm'.format(n, cm, mm))

print('{}km -> {}hm -> {}dam -> {:.0f}m -> {:.0f}dm -> {:.0f}cm -> {:.0f}mm'.format((n / 1000), (n / 100), (n / 10), n, (n * 10), (n * 100), (n * 1000)))
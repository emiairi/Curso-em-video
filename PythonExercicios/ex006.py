# Desafio 006
''' Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada'''

n = int(input('Digite um valor: '))
print('O dobro é: {}.\nO triplo é: {}'.format((n * 2), (n * 3)))
# print('O triplo é: {}'.format(n * 3))
# print('A raiz quadrada é: {:.2f}'.format(n ** (1/2)))
print('A raiz quadrada é: {:.2f}'.format(pow(n, (1/2))))
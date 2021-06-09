# Desafio 060 - Cálculo do Fatorial

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex.: 5! = 5x4x3x2x1 = 120'''

'''n = int(input('Digite um número: '))
fatorial = 1
print('{}! ='.format(n), end=' ')

while n != 0:
    fatorial *= n
    print('{} x '.format(n), end='')
    n -= 1

print('= {}' .format(fatorial))'''

# --------------------------------
# Resolução Guanabara 1
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {}! é {}'.format(n, f))'''

# --------------------------------
# Resolução Guanabara 2
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

#--------- Desafio extra -----------
# Usando for
n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')

for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))

# Desafio 052 - Números Primos

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Digite um valor: '))

count = 0

if n == 2:
    print('2 é primo')
elif n % 2 != 0:
    for c in range(2, n):
        if n % c == 0:
           # print('{} -> {}' .format(n, c))
            count += 1

#print('Contador {}' .format(count))

if count == 0:
    print('{} é um número primo.' .format(n))
else:
    print('{} não é um número primo.' .format(n))



'''Solução Guanabara
num = int(input('Digite umm número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes' .format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO!!!')
else:
    print('E por isso ele NÃO É PRIMO!!!')
'''
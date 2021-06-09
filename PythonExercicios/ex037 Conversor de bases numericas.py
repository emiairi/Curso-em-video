# Desafio 037 - Conversor de bases numéricas

"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
    -> 1 para binário
    -> 2 para octal
    -> 3 para hexadecimal"""
from builtins import print
from time import sleep

num = int(input('Digite um número inteiro: '))
print('Digite qual a base de conversão que deseja utilizar.')
print(' 1 - Binário \n 2 - Octal \n 3 - Hexadecimal')
print('''Escolha uma das bases para conversão:
[ 1 ] cpnverter para BINÁRIO
[ 2 ] converte para OCTAL
[ 3 ] converte para HEXADECIMAL''')
base = int(input('Opção: '))

print('\033[1;36mCONVERTENDO...\033[m')
sleep(2)

if base == 1:
    print('{} para binário {}' .format(num, bin(num)[2:]))
elif base == 2:
    print('{} para octal {}' .format(num, oct(num)[2:]))
elif base == 3:
    print('{} para hexadecimal {}'.format(num, hex(num)[2:]))
else:
    print('Base incorreta!')
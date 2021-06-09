# Desafio 048 - Soma ímpares múltiplos de três

'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.'''

s = 0
co = 0

for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            s += c

for n in range(3, 501, 3):
    if n % 2 != 0:
        co += n
        print(n, end=' ')

print('\nA soma dos números ímpares e múltiplos de três no intervalo de 1 até 500 é: \033[1;31m{}\033[m\n' .format(s))
print('A soma dos números ímpares e múltiplos de três no intervalo de 1 até 500 é: \033[1;31m{}\033[m' .format(co))

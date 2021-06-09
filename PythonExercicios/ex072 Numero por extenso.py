# Desafio 072 - Número por Extenso

'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''

números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número \033[1;31m{números[n]}\033[m.')
        cont = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
        while cont not in 'SN':
            print('Opção inválida!')
            cont = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
        if cont == 'N':
            break
    else:
        print('Tente novamente.')
print('Fim do programa.')

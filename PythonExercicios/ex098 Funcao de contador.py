# Desafio 098 - Função de Contador

'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) Uma contagem personalizada.'''
from time import sleep

def contador(início, fim, passo):
    print('-=' * 20)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
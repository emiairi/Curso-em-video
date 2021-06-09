# Desafio 099 - Função que descobre o maior

'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def analisador(* valores):
    print('-=' * 25)
    tam = len(valores)
    print('Analisando os valores passados: ')
    maior = 0
    for i in valores:
        if i > maior:
            maior = i
        print(i, end=' ')
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


analisador(2, 9, 4, 5, 7, 1)
analisador(4, 7, 0)
analisador(1, 2)
analisador(6)
analisador()
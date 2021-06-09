# Desafio 097 - Um print especial

'''Faça um programa que tenha uam função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.'''

def título(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


título('Gustavo Guanabara')
título('Curso de Python no YouTube')
título('CeV')
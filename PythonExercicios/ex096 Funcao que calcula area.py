# Desafio 096 - Função que calcula área

'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e
comprimento) e mostre a área do terreno.'''

def área(largura, comprimento):
    s = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {s:.1f} m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
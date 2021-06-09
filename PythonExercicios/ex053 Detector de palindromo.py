# Desafio 053 - Detector de Palíndromo

'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).replace(" ", "").lower()

tamanho = len(frase)
#inverso = ''
inverso = frase[::-1]

'''for letra in range(tamanho - 1, -1, -1):
    inverso += frase[letra]'''

if frase == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')

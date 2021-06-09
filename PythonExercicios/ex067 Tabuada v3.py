# Desafio 067 - Tabuada v3.0

'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-' * 40)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c:2} = {tabuada * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


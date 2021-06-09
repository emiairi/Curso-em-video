# Desafio 079 - Valores únicos em uma Lista

'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exiidos todos os valores únicos digitados, em ordem crescente.'''

listval = []

while True:
    aux = int(input('Digite um valor: '))
    if aux in listval:
        print('Valor duplicado! Não vou adicionar...')
    else:
        listval.append(aux)
        print('Valor adicionado com sucesso...')

    continuar = str(input('Quer continuar? [S/N]? ')).strip().upper()

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]? ')).strip().upper()

    if continuar in 'N':
            break

listval.sort()
print('-=' * 20)
print(f'Você digitou os valores {listval}')

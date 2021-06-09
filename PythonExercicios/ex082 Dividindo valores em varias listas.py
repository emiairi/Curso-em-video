# Desafio 082 - Dividindo valores em várias listas

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.'''

numeros = []
par = []
impar = []

while True:
    numeros.append(int(input('Digite um número: ')))
    cont = str(input('Quer continuar? [S/N]')).strip().upper()

    while cont not in 'SN' or cont in ' ':
        cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont in 'N':
        break

for c in numeros:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
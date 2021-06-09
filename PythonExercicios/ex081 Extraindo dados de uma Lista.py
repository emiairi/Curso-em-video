# Desafio 081 - Extraindo dados de uma Lista

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenados de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    while continuar not in 'NS' or continuar in ' ':
        print('Opção inválida.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()

    if continuar in 'N':
        break

print('-=' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')

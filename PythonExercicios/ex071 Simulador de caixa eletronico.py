# Desafio 071 - Simulador de Caixa Eletrônico

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$ '))
cinquenta = vinte = dez = um = 0

while valor < 0:
    print('Valor inválido.')
    valor = int(input('Qual valor você quer sacar? R$ '))

cinquenta = valor / 50
print(f'Total de {int (cinquenta)} cédulas de R$ 50')
valor = valor % 50
vinte = valor / 20
print(f'Total de {int (vinte)} cédulas de R$ 20')
valor = valor % 20
dez = valor / 10
print(f'Total de {int (dez)} cédulas de R$ 10')
valor = valor % 10
um = valor
print(f'Total de {int (um)} cédulas de R$ 1')

#--- SOLUÇÃO GUANABARA UTILIZANDO WHILE ---
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!!!')

#--- Solução FOR comentário vídeo ---
valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in[50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')


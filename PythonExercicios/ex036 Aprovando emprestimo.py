# Desafio 036 - Aprovando Empréstimos

"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
    negado."""

print('*-' * 20)
print(' ' * 10, 'EMPRÉSTIMO BANCÁRIO')
print('*-' * 20)

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Salário do comprador R$ '))
anos = int(input('Em quantos anos pretende pagar a casa? '))

# Cálculo de 30% do salário
porcentagemSalario = salario * 0.3

prestacao = casa / (anos * 12)

print('O valor mensal da prestação será de: R$ {:.2f}' .format(prestacao))

if prestacao > porcentagemSalario:
    print('O empréstimo foi \033[1;31mnegado\033[m.')
else:
    print('\033[1;32mPARABÉNS!!!\033[m O empréstimo foi \033[1;32maprovado\033[m.')

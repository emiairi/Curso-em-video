# Desafio 057 - Validação de dados

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores  M ou F. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

s = str(input('Sexo [F/M]: ')).strip().upper()[0]

#while s != 'F' and s != 'M':
while s not in 'MmFf':
    print('Opção inválida. Tente novamente.')
    s = str(input('Sexo [F/M]: ')).strip().upper()[0] #Caso o usuário digite 'masculino' ou 'feminino'.

if s == 'F':
    print('Sexo: Femino')
else:
    print('Sexo Masculino')

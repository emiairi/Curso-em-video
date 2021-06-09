# Desafio 069 - Análise de dados do grupo

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.'''

tot18 = totH = totM20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))

    # Verifica quantas pessoas tem mais de 18 anos.
    if idade > 18:
        tot18 += 1

    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]

    while sexo not in 'MF':
        print('Opção inválida. Tente novamente.')
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]

    # Verifica quantos homens foram cadastrados.
    if sexo == 'M':
        totH += 1
    else: # Verifica quantas mulheres tem menos de 20 anos.
        if idade < 20:
            totM20 += 1

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção inválida. Tente novamente.')
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    # Condição de saída do programa
    if continuar == 'N':
        break

print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')

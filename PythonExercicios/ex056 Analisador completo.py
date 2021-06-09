# Desafio 056 - Analisador Completo

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.'''

somaidade = 0
maior = 0
cont = 0

for c in range(1, 5):
    print('------ {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()

    somaidade += idade
    if sexo.upper() == 'M':
        if idade > maior:
            maior = idade
            nomeVelho = nome
    elif sexo.upper() == 'F':
        if idade < 20:
            cont += 1
    else:
        print('Opção inválida.')

print('A média das idades é {}.' .format(somaidade / 4))
print('O homem mais velho tem é {} e tem {} anos.' .format(nomeVelho, maior))
print('{} mulheres tem menos de 20 anos.' .format(cont))

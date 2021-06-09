# Desafio 094 - Unindo dicionários e listas

'''Crie um programa que leia nome, sexo e idade de várias pessoas, guradando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas cadastradas;
b) A média de idade;
c) Uma lista com mulheres;
d) Uma lista com idade acima da média.'''

dados = list()
pessoas = dict()
sidade = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while pessoas['sexo'] not in 'MF' or pessoas['sexo'] in ' ':
        print('\033[1;31mERRO! Por favor, digite apenas M ou F.\033[m')
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    pessoas['idade'] = int(input('Idade: '))
    sidade += pessoas['idade']
    dados.append(pessoas.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN' or resp in ' ':
        print('\033[1;31mERRO! Responda apenas S ou N.\033[m')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos \033[1;34m{len(dados)}\033[m pessoas cadastradas.')
média = sidade / len(dados)
print(f'A média de idade é de {média:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for d in dados:
    if d['sexo'] == 'F':
        print(d['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média:')
for d in dados:
    if d['idade'] >= média:
        for k, v in d.items():
            print(f'    {k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
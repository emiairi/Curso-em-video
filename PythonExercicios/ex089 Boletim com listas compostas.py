# Desafio 089 - Boletim com listas compostas

'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos= list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])
    cont = str(input('Quer continuar? [S/N]? ')).strip().upper()
    while cont not in 'SN' or cont in ' ':
        cont = str(input('Quer continuar? [S/N]? ')).strip().upper()
    if cont == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for c, v in enumerate(alunos):
    if v[2] < 7:
        print(f'{c:<4}{v[0]:<10}\033[1;31m{v[2]:>8.1f}\033[m')
    else:
        print(f'{c:<4}{v[0]:<10}\033[1;34m{v[2]:>8.1f}\033[m')

while True:
    print('-' * 30)
    nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota == 999:
        print('FINALIZANDO....')
        break
    if nota <= len(alunos) - 1:
        print(f'Notas de {alunos[nota][0]} são {alunos[nota][1]}')

print('<<< VOLTE SEMPRE >>>')
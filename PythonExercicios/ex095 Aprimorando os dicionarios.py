# Desafio 095 - Aprimorando os Dicionários

'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''

jogador = {}
gols = []
time = list()
total = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    gols.clear()
    while resp not in 'SN' or resp == '':
        print('\033[1;31mOpção inválida. Escolha S ou N.\033[m')
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if resp in 'N':
        break
print('-=' * 30)
#print('cod nome     gols            total')
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
'''for c, v in enumerate(time):
    print(c, end=' ')
    for k, i in v.items():
        print(f'{i}', end='     ')
    print()'''
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    if dados >= len(time):
        print(f'ERRO! Não existe jogador com código {dados}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}')
        for i, g in enumerate(time[dados]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
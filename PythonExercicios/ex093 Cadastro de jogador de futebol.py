# Desafio 093 - Cadastro de Jogador de Futebol

'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.') # Guanabara: ...jogou {len(jogador["gols"])}
for c, v in enumerate(gols): # Guanabara: for i, v in enumerate(jogador["gols"])
    print(f'    => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

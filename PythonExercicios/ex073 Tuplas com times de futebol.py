# Desafio 073 - Tuplas com Times de Futebol

'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoense.'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico Paranaense',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo',
         'Ceará', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')

print(f'Os primeiros cinco colocados são: {times[0:5]}')
print(f'Os quatro últimos colocados são: {times[-4:]}')
print(f'Lista em ordem alfabética: {sorted(times)}')
print(f'Chapecoense está na {times.index("Chapecoense") + 1}ª')
for posição in range(0, len(times)):
    if times[posição] == 'Chapecoense':
        print(f'Chapecoense está na {posição + 1}ª posição da tabela')

# Desafio 068 - Jogo do Par ou Ímpar

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitoria = 0

while True:
    print('-=' * 15)
    jogador = int(input('Diga um valor: '))
    jogada = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]

    # Verifica se a jogada é válida.
    while jogada not in 'PpIi':
        print('Jogada inválida. Tente novamente.')
        jogada = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]

    # Valor que o computador escolhe
    computador = randint(0, 10)
    soma = computador + jogador

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}', end='. ')
    print('DEU PAR.' if soma % 2 == 0 else 'DEU ÍMPAR.')
    print('-' * 30)
    if soma % 2 == 0:
        if jogada == 'P':
            print('Você VENCEU!!\nVamos jogar novamente...')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    else:
        if jogada == 'I':
            print('Você VENCEU!!\nVamos jogar novamente...')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes.')


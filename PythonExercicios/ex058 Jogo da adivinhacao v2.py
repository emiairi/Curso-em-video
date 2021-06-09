# Desafio 058 - Jogo da Adivinhação v2.0

'''Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

computador = randint(0, 10)
jogador = int(input('Tente adivinhar o número que estou pensando: '))
jogadas = 1

while jogador != computador or jogador > 10:
    if jogador > 10:
        print('Valor inválido!')
    else:
        if jogador > computador:
            print('Não foi dessa vez. Continue tentando! Dica: é menor')
        else:
            print('Não foi dessa vez. Continue tentando! Dica: é maior')
        jogadas += 1
    jogador = int(input('Tente adivinhar o número que estou pensando: '))

print('-' * 30)
print('Parabéns! Você acertou o número {} na {}ª tentativa.' .format(computador, jogadas))

# Solução Guanabara
'''from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))'''
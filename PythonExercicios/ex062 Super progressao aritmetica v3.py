# Desafio 062 - Super Progressão Aritmética v3.0

'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao

# Dez primeiros termos.
while primeiro <= decimo:
    print(primeiro, end=' ')
    primeiro += razao

numerotermos = 10
termo = 1
while termo != 0:
    print('\033[1;31mPAUSA\033[m')
    termo = int(input('Quantos termos você quer mostrar mais? '))
    numerotermos += termo
    calculo = primeiro + (termo - 1) * razao
    while primeiro <= calculo:
        print(primeiro, end=' ')
        primeiro += razao
print('Progressão finalizada com \033[1;35m{}\033[m termos mostrados.' .format(numerotermos))

#---------------------
# Solução Guanabara
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.' .format(total))


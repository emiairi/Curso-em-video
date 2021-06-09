# Desafio 035 - Analisando Triângulo v 1.0

"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

'''if(abs(r2 - r3) < r1 < (r2 + r3)):
    if(abs(r1 - r3) < r2 < (r1 + r2)):
        if(abs(r1 - r2) < r3 < (r1 + r2)):
            print('Triângulo')
else:
    print('Não é triângulo')'''

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

if abs(r2-r3)<r1<(r2+r3) and abs(r1-r3)<r2<(r1+r2) and abs(r1-r2)<r3<(r1+r2):
    print('-> Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('-> Os segmentos acima NÃO PODEM FORMAR triângulo!')

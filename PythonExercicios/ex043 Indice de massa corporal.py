# Desafio 043 - Índice de massa corporal

"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:
    -> Abaixo de 18.5: Abaixo do peso
    -> Entre 18.5 e 25: Peso ideal
    -> 25 até 30: Sobrepeso
    -> 30 até 40: Obesidade
    -> Acima de 40: Obesidade mórbida"""

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual o sua altura? '))

imc = peso / (altura ** 2)

print('Seu IMC é {:.1f}.' .format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
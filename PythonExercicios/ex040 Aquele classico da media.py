# Desafio 040 - Aquele clássico da média

"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a média atingida:
    -> Média abaixo de 5.0: REPROVADO.
    -> Média entre 5.0 e 6.9: RECUPERAÇÃO.
    -> Média 7.0 ou superior: APROVADO."""

cores = {'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'pretobranco': '\033[7;30m',
         'limpa': '\033[m'}

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2)/2
print('Sua média é: {}{:.1f}{}.' .format(cores['pretobranco'], media, cores['limpa']))

if media < 5:
    print('{}REPROVADO{}' .format(cores['vermelho'], cores['limpa']))
elif 5 <= media < 7:
    print('{}RECUPERAÇÃO{}' .format(cores['amarelo'], cores['limpa']))
else:
    print('{}APROVADO{}' .format(cores['verde'], cores['limpa']))
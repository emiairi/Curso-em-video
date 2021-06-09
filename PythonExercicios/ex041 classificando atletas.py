# Desafio 041 - Classificando atletas

"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade.
    -> Até 9 anos: MIRIM
    -> Até 14 anos: INFANTIL
    -> Até 19 anos: JÚNIOR
    -> Até 40 anos: SÊNIOR
    -> Acima: MASTER"""

from datetime import date

cores = {'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m',
         'ciano':   '\033[1;36m',
         'invverde': '\033[7;32m',
         'limpa': '\033[m'}

anoAtual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = anoAtual - ano

print('Você tem {}{} anos{}.' .format(cores['invverde'], idade, cores['limpa']))

if ano < 1900 or ano > anoAtual:
    print('{}Ano incorreto!!!{}' .format(cores['vermelho'], cores['limpa']))
elif idade <= 9:
    print('Você está na categoria {}MIRIM{}.' .format(cores['roxo'], cores['limpa']))
elif idade <= 14:
    print('Você está na categoria {}INFANTIL{}.' .format(cores['ciano'], cores['limpa']))
elif idade <= 19:
    print('Você está ma categoria {}JÚNIOR{}.' .format(cores['azul'], cores['limpa']))
elif idade <=40:
    print('Você está na categoria {}SÊNIOR{}.' .format(cores['amarelo'], cores['limpa']))
else:
    print('Você está na categoria {}MASTER{}.' .format(cores['branco'], cores['limpa']))
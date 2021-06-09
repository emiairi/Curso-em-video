# Desafio 039 - Alistamento Militar

"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    -> Se ele ainda vai se alistar ao serviço militar.
    -> Se é a hora de se alistar.
    -> Se já passou do tempo do alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

cores = {'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[m'}
print('Qual o sexo?\nm - masculino\nf - feminino')
sexo = str(input('Opção: '))

if sexo.lower() == 'm':

    ano = int(input('Qual o seu ano de nascimento? '))
    anoAtual = date.today().year
    idade = anoAtual - ano

    print('Você tem {} anos em {}.'.format(idade, anoAtual))

    if ano < 1900 or ano > anoAtual:
        print('{}Ano incorreto.{}'.format(cores['vermelho'], cores['limpa']))
    elif idade < 18:
        print('Faltam {}{}{} anos para o alistamento.\nSeu alistamento será no ano {}.'
              .format(cores['azul'], 18 - idade, cores['limpa'], ano + 18))
    elif idade > 18:
        print('Já passaram {}{}{} anos para o alistamento.\nSeu alistamento foi em {}.'
              .format(cores['vermelho'], idade - 18, cores['limpa'], ano + 18))
    else:  # idade == 18
        print('Hora de se alistar.')
elif sexo.lower() == 'f':
    print('O alistamento não é obrigatório.')
else:
    print('Opção inválida!!!!')

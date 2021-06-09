# Desafio 092 - Cadastro de Trabalhador em Python

'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário se
por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date

trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
trabalhador['idade'] = date.today().year - ano
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$ '))
    aposent = (trabalhador['contratação'] + 35) - ano
    trabalhador['aposentadoria'] = aposent
print('-=' * 30)

for k, v in trabalhador.items():
    print(f'   - {k} tem o valor {v}')

# ---- GUANABARA
# from datetime import datetime
# = datetime.now().year
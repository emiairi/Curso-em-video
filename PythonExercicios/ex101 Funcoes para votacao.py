# Desafio 101 - Funções para votação

'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmentro o ano de nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA!'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    return idade


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

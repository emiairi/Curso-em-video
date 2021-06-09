# Desafio 105 - Analisando e gerando Dicionários

'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma;
- A situação (opcional).
Adicione também as docstrings.'''


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/len(n)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic
    '''maior = menor = média = 0
    cont = soma = 0
    tam = len(n)

    for nota in n:
        if cont == 0:
            maior = nota
            menor = nota
            cont += 1
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
        soma += nota
    média = soma/tam

    if média <= 5:
        situ = 'RUIM'
    elif média >=7:
        situ = 'BOA'
    else:
        situ = 'RAZOÁVEL'

    if sit == False:
        dic = {'total': tam, 'maior': maior, 'menor': menor, 'média': média}
    else:
        dic = {'total': tam, 'maior': maior, 'menor': menor, 'média': média, 'situação': situ}
    return dic'''


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

# Desafio 044 - Gerenciador de Pagamento

"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de
pagamento:
    -> à vista dinheiro/cheque: 10% de desconto
    -> à vista no cartão: 5% de desconto
    -> em até 2x no cartão: preço normal
    -> 3x ou mais no cartão: 20% de juros."""

print('{:=^40}' .format(' LOJA A '))

cores = {'branco': '\033[1;30m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'azul': '\033[1;34m',
         'roxo': '\033[1;35m',
         'ciano':   '\033[1;36m',
         'limpa': '\033[m'}

produto = float(input('Qual o valor do produto? R$ '))

print('Escolha uma forma de pagamento: ')
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque com 10% de desconto
[ 2 ] à vista no cartão com 5% de desconto
[ 3 ] em até 2x no cartão sem desconto
[ 4 ] 3x ou mais no cartão com 20% de juros''')
'''print('1 - à vista dinheiro/cheque com {}10% de desconto{} \n2 - à vista no cartão com {}5% de desconto{}'
      .format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
print('3 - em até 2x no cartão {}sem desconto{} \n4 - 3x ou mais no cartão com {}20% de juros{}'
      .format(cores['roxo'], cores['limpa'], cores['vermelho'], cores['limpa']))'''
opcao = int(input('Escolha: '))

if opcao == 1:
    total = produto - (produto * 0.10)
elif opcao == 2:
    total = produto - (produto * 0.05)
elif opcao == 3:
    total = produto
    print('O valor parcelado em 2x será de R$ {:.2f}' .format(total / 2))
elif opcao == 4:
    total = produto + (produto * 0.20)
    parcela = int(input('Quantas parcelas? '))
    print('O valor parcelado em {}x será de R$ {:.2f}.' .format(parcela, total / parcela))
else:
    print('Opção inválida!!!')

print('\nO valor final do produto será R$ {:.2f}' .format(total))

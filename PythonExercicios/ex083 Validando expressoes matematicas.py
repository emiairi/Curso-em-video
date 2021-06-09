# Desafio 083 - Validando expressões matemáticas

'''Crie um programa onde o usuário digite uma expressão qualquer e use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses aberto e fechado na ordem correta.'''

expressão = str(input('Digite a expressão: '))
aberto = fechado = 0
for c in expressão:
    if c in '(':
        aberto += 1
    if c in ')':
        fechado += 1
if aberto == fechado:
    print('Sua expressão está váilida!')
else:
    print('Sua expressão está errada!')

# ---- Solução Guanabara -----
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


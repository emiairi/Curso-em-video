# Desafio 080 - Lista ordenada sem repetições

'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
 correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.'''

num = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0:
        # Primeiro valor adicionado.
        num.append(valor)
        print("Primeiro elemento adicionado na lista...")
    else:
        # Verifica se o número existe na lista.
        while True:
            if valor in num:
                print('Valor já existe na lista.')
                valor = int(input('Digite um valor: '))
            else:
                break
        if valor > num[-1]: # Último elemento da lista num[-1]
            num.insert(len(num), valor)
            print("Adicionado ao final da lista...")
        for c in range(0, len(num)):
            if valor < num[c]:
                num.insert(c, valor)
                print(f'Adicionado na posição {c} da lista...')
                break

print(num)

# ---- Guanabara ----
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valore digitados em ordem foram {lista}')

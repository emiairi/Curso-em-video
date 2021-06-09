# Desafio 022 - Analisador de Textos.

"""Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas
-> O nome com todas as letras minúsculas
-> Quantas letras ao todos (sem considerar espaços)
-> Quantas letras tem o primeiro nome"""

nome = str(input('Qual o seu nome completo? ')).strip()

print(nome.upper())
print(nome.lower())
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print(nome.find(' '))
separanome = nome.split()
print('O primeiro nome é {} e tem {} caracteres.'.format(separanome[0], len(separanome[0])))

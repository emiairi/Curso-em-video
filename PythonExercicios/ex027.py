# Desafio 027 - Primeiro e último nome de uma pessoa.

"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
EX.: Ana Maria de Souza
primeiro: Ana
último: Souza"""

nome = str(input('Escreva o seu nome completo: ')).strip()
listanome = nome.split()
print('O primeiro nome é: {}'.format(listanome[0].capitalize()))
print('O último nome é: {}'.format(listanome[len(listanome) - 1].capitalize()))

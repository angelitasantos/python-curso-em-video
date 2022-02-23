'''
# Desafio 025

Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''


nome = str(input('Qual é o seu nome completo? ')).strip()
palavra = 'SILVA'
validacao = palavra in nome.upper()
print(f'O seu nome tem {palavra}? {validacao}')
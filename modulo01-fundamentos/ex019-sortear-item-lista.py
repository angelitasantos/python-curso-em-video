'''
# Desafio 019

Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''


import random

aluno_01 = str(input('Digite o primeiro aluno: '))
aluno_02 = str(input('Digite o segundo aluno: '))
aluno_03 = str(input('Digite o terceiro aluno: '))
aluno_04 = str(input('Digite o quarto aluno: '))
lista = [aluno_01, aluno_02, aluno_03, aluno_04]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')


from random import choice

aluno_01 = str(input('Digite o primeiro aluno: '))
aluno_02 = str(input('Digite o segundo aluno: '))
aluno_03 = str(input('Digite o terceiro aluno: '))
aluno_04 = str(input('Digite o quarto aluno: '))
lista = [aluno_01, aluno_02, aluno_03, aluno_04]
escolhido = choice(lista)

print(f'O aluno escolhido foi: {escolhido}')
'''
# Desafio 020

Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''


import random

aluno_01 = str(input('Digite o primeiro aluno: '))
aluno_02 = str(input('Digite o segundo aluno: '))
aluno_03 = str(input('Digite o terceiro aluno: '))
aluno_04 = str(input('Digite o quarto aluno: '))
lista = [aluno_01, aluno_02, aluno_03, aluno_04]
random.shuffle(lista)

print(f'A ordem de apresentação será:')
print(lista)


from random import shuffle

aluno_01 = str(input('Digite o primeiro aluno: '))
aluno_02 = str(input('Digite o segundo aluno: '))
aluno_03 = str(input('Digite o terceiro aluno: '))
aluno_04 = str(input('Digite o quarto aluno: '))
lista = [aluno_01, aluno_02, aluno_03, aluno_04]
shuffle(lista)

print(f'A ordem de apresentação será:')
print(lista)
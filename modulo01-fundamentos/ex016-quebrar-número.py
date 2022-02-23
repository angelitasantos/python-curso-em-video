'''
# Desafio 016

Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''


import math

numero = float(input('Digite um valor: '))
porcao_inteira = math.trunc(numero)
print(f'O valor digitado foi {numero} e a sua porção inteira é {porcao_inteira}.')


from math import trunc

numero = float(input('Digite um valor: '))
porcao_inteira = trunc(numero)
print(f'O valor digitado foi {numero} e a sua porção inteira é {porcao_inteira}.')


numero = float(input('Digite um valor: '))
porcao_inteira = int(numero)
print(f'O valor digitado foi {numero} e a sua porção inteira é {porcao_inteira}.')
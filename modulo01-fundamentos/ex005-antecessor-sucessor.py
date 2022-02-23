'''
# Desafio 005

Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''


numero_inteiro = int(input('Digite um número inteiro: '))
antecessor = numero_inteiro - 1
sucessor = numero_inteiro + 1
print(f'Analisando o número {numero_inteiro}: seu antecessor é {antecessor} e seu sucessor é {sucessor}')


numero = int(input('Digite um número inteiro: '))
print(f'Analisando o número {numero}: seu antecessor é {numero - 1} e seu sucessor é {numero + 1}')
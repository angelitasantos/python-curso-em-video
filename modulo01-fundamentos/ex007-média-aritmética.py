'''
# Desafio 007

Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''


qtde_notas = 2
nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))
media = (nota_01 + nota_02) / qtde_notas
print(f'A média entre {nota_01:.1f} e {nota_02:.1f} é igual a: {media:.1f}.')
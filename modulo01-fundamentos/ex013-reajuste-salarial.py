'''
# Desafio 013

Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''


salario = float(input('Digite o salário do funcionário: R$ '))
reajuste = 15
valor_reajuste = salario * reajuste / 100
novo_salario = salario + valor_reajuste

print(f'Um funcionário que recebe R$ {salario:.2f}, com {reajuste}$ de aumento, passará a receber R$ {novo_salario:.2f}')
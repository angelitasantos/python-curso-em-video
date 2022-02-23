'''
# Desafio 034

Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''


salario = float(input('Digite o salário do funcionário: R$ '))

salario_base = 1250
aumento_superiores = 10
aumento_inferiores = 15

if salario <= salario_base:
    novo_salario = salario + (salario * aumento_inferiores / 100)
else:
    novo_salario = salario + (salario * aumento_superiores / 100)

print(f'Quem ganha R$ {salario:.2f} passará a ganhar R$ {novo_salario:.2f}.')
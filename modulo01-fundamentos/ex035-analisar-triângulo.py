'''
# Desafio 035

Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.
'''


print('-' * 100)
print('Analisador de Triângulos...')
print('-' * 100)

reta_01 = float(input('Digite a primeira reta: '))
reta_02 = float(input('Digite a segunda reta: '))
reta_03 = float(input('Digite a terceira reta: '))

if reta_01 < reta_02 + reta_03 and reta_02 < reta_01 + reta_03 and reta_03 < reta_01 + reta_02:
    print('As retas acima PODEM formar um Triângulo.')
else:
    print('As retas acima NÃO PODEM formar um Triângulo.')
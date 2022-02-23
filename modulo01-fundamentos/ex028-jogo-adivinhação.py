'''
# Desafio 028

Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever
na tela se o usuário venceu ou perdeu.
'''


from random import randint
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
print('-=-' * 30)

computador = randint(0,5)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO ...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print(f'VOCÊ PERDEU! Eu pensei no número {computador} e não no número {jogador}.')
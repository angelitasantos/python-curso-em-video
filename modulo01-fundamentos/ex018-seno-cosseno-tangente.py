'''
# Desafio 018

Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''


import math
# seno, cosseno e tangente estão em radianos

angulo = float(input('Digite o ângulo que você deseja: '))
# converter o angulo em graus para radianos
angulo_radiano = math.radians(angulo)
seno = math.sin(angulo_radiano)
cosseno = math.cos(angulo_radiano)
tangente = math.tan(angulo_radiano)

print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}.')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}.')
print(f'O ângulo de {angulo}° tem o TANGENTE de {tangente:.2f}.')


from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
angulo_radiano = radians(angulo)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)

print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}.')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}.')
print(f'O ângulo de {angulo}° tem o TANGENTE de {tangente:.2f}.')
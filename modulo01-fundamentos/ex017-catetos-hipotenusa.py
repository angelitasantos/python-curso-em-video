'''
# Desafio 017

Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''


cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1 / 2)

print(f'A hipotenusa do triângulo retângulo mede: {hipotenusa:.2f}.')


import math

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do triângulo retângulo mede: {hipotenusa:.2f}.')


from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa do triângulo retângulo mede: {hipotenusa:.2f}.')
'''
# Desafio 011

Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''


largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem dimensão de {largura}m x {altura}m e sua área é de {area}m².')
print(f'Para pintar esta parede, você precisará de {tinta:.2f}L de tinta.')
'''
# Desafio 014

Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''


celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = ((9 * celsius) / 5 ) + 32
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F.')


fahrenheit = float(input('Informe a temperatura em °F: '))
celsius = (fahrenheit - 32) / (9 / 5)
print(f'A temperatura de {fahrenheit}°F corresponde a {celsius}°C.')
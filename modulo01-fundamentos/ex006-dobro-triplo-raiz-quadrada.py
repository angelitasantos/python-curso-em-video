'''
# Desafio 006

Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''


numero = int(input('Digite um número inteiro: '))
print(f'O dobro de {numero} vale {numero * 2}')
print(f'O tripo de {numero} vale {numero * 3}')
print(f'A raiz quadrada de {numero} é igual a {numero ** (1 / 2):.2f}')


numero = int(input('Digite um número inteiro: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1 / 2)
print(f'O dobro de {numero} vale {dobro}')
print(f'O tripo de {numero} vale {triplo}')
print(f'A raiz quadrada de {numero} é igual a {raiz_quadrada:.2f}')


numero = int(input('Digite um número inteiro: '))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = pow(numero, (1 / 2))
print(f'O dobro de {numero} vale {dobro}')
print(f'O tripo de {numero} vale {triplo}')
print(f'A raiz quadrada de {numero} é igual a {raiz_quadrada:.2f}')

'''
# Desafio 012

Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''


preco = float(input('Qual é o preço do produto? R$ '))
desconto = 5
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto
print(f'O produto que custa R$ {preco:.2f}, com desconto de {desconto}%, custará R$ {preco_final:.2f}.')
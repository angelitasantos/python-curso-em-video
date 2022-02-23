'''
# Desafio 015

Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$ 60 por dia e R$ 0,15 por Km rodado.
'''


dias = int(input('Quantos dias alugados: '))
km_percorrido = float(input('Quantos km rodados: '))

aluguel_dia = 60
valor_km_rodado = 0.15

valor = aluguel_dia * dias + valor_km_rodado * km_percorrido
print(f'O total a pagar é de R$ {valor:.2f}')
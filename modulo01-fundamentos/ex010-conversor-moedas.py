'''
# Desafio 010

Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''


real = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao_dia_dolar = 3.27
cotacao_dia_euro = 3.85
dolar = real / cotacao_dia_dolar
euro = real / cotacao_dia_euro

print(f'Com R$ {real:.2f} reais você pode comprar U$$ {dolar:.2f} dolares.')
print(f'Com R$ {real:.2f} reais você pode comprar €$ {euro:.2f} euros.')
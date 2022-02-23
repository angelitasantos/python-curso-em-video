'''
# Desafio 031

Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''


distancia = float(input('Qual é a distância da sua viagem? '))

viagem_curta = 0.50
viagem_longa = 0.45

km_viagem_curta = 200

if distancia <= km_viagem_curta:
    preco = distancia * viagem_curta
else:
    preco = distancia * viagem_longa

print(f'Você está prestes a começar uma viagem de {distancia}km,')
print(f'e o preço da sua passagem será de R$ {preco:.2f}.')



distancia = float(input('Qual é a distância da sua viagem? '))

viagem_curta = 0.50
viagem_longa = 0.45

km_viagem_curta = 200

preco = distancia * viagem_curta if distancia <= km_viagem_curta else distancia * viagem_longa

print(f'Você está prestes a começar uma viagem de {distancia}km,')
print(f'e o preço da sua passagem será de R$ {preco:.2f}.')
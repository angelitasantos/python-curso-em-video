'''
# Desafio 029

Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''


velocidade = float(input('Qual é a velocidade atual do carro? '))

velocidade_maxima = 80
multa_km = 7
valor_multa = (velocidade - velocidade_maxima) * multa_km

if velocidade > velocidade_maxima:
    print('-' * 100)
    print(f'\033[1;31;43mMULTADO!\033[m')
    print(f'\033[1;31mVocê ultrapassou o limite de velocidade de \033[0;33;45m{velocidade_maxima}km/h.\033[m')
    print(f'\033[0;31mVocê deve pagar uma multa no valor de \033[1;31;43mR$ {valor_multa:.2f}\033[m.')

print('\033[0;32mTenha um bom dia e dirija com segurança.\033[m')
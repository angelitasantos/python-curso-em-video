'''
# Desafio 024

Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''


cidade = str(input('Em que cidade você nasceu? ')).strip()
# .strip() = remove os espaços em branco no início e no fim do texto
palavra = 'SANTO'
validacao = {cidade[:5].upper()} == {palavra}

print(f'O nome da cidade que você nasceu começa com a palavra {palavra}? {validacao}')
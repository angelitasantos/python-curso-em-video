'''
# Desafio 026

Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''


frase = str(input('Digite uma frase: ')).strip().upper()
letra = 'A'
qtde_aparece = frase.count(letra)

primeira_letra = frase.find(letra) + 1
ultima_letra = frase.rfind(letra) + 1

print(f'A letra {letra} aparece {qtde_aparece} vezes na frase.')
print(f'A primeira letra {letra} aparece na posição {primeira_letra}.')
print(f'A última letra {letra} aparece na posição {ultima_letra}.')
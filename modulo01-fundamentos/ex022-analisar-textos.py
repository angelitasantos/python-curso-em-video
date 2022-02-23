'''
# Desafio 022

Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''


nome = str(input('Digite seu nome completo: ')).strip()
nome_upper = nome.upper()
nome_lower = nome.lower()
quantas_letras = len(nome) - nome.count(' ') # sem espaços entre as palavras
letras_primeiro_nome = nome.find(' ')
separa_nome = nome.split()
primeiro_nome = separa_nome[0]
ultimo_nome = separa_nome[-1]

print('-' * 100)
print(f'Analisando seu nome ...')
print(f'Seu nome em letras maiúsculas é: {nome_upper}')
print(f'Seu nome em letras minúsculas é: {nome_lower}')
print(f'Seu nome tem ao todo {quantas_letras} letras.')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {letras_primeiro_nome} letras.')
print(f'Seu último nome é {ultimo_nome}.')
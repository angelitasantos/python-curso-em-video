'''
# Desafio 027

Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
'''


nome = str(input('Digite seu nome completo: ')).strip()
separa_nome = nome.split()
primeiro_nome = separa_nome[0]
ultimo_nome = separa_nome[len(separa_nome) - 1]

print('-' * 100)
print(f'Analisando seu nome ...')
print(f'Seu primeiro nome é {primeiro_nome}.')
print(f'Seu último nome é {ultimo_nome}.')
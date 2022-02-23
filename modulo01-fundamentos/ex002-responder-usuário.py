'''
# Desafio 002

Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
'''


nome = str(input('Digite o seu nome: '))
print('É um prazer te conhecer,', nome)


nome2 = str(input('Digite o seu nome: '))
sobrenome2 = str(input('Digite o seu sobrenome: '))
print(f'{nome2} {sobrenome2}')


nome3 = str(input('Digite o seu nome: '))
sobrenome3 = str(input('Digite o seu sobrenome: '))
nome_completo = nome3 + ' ' + sobrenome3
print(f'Bom dia, {nome_completo}')


def responder_usuario():
    nome4 = 'Angelita'
    mensagem = 'É um prazer te conhecer,'
    return f'{mensagem} {nome4}'

print(responder_usuario())


class BoasVindas:

    def __init__(self, mensagem1):
        self.mensagem1 = mensagem1

    def responder_usuario(self):
        print(f'Anderson, {self.mensagem1}')

instancia = BoasVindas('seja bem vindo!')
instancia.responder_usuario()
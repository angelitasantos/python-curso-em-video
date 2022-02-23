'''
# Desafio 001

Exercício Python 001: Crie um programa que escreva "Olá mundo" na tela.
'''


print('Olá mundo!')


mensagem1 = 'Primeira mensagem no Python!'
print(mensagem1)


nome2 = str(input('Digite seu nome: '))
mensagem2 = 'Bom dia,'
print(mensagem2, nome2)


nome3 = str(input('Digite seu nome: '))
mensagem3 = 'Seja bem-vindo(a)'
print(f'{mensagem3}, {nome3}')


def tudo_pronto():
    nome4 = str(input('Digite seu nome: '))
    mensagem4 = 'Esta é a minha primeira função, '
    return f'{mensagem4}{nome4}'

print(tudo_pronto())


class TudoPronto():

    def __init__(self, nome5, mensagem5):
        self.nome5 = nome5
        self.mensagem5 = mensagem5

    def __repr__(self):
        return f'{self.nome5}, {self.mensagem5}'


instancia = TudoPronto('Angelita', 'esta é a minha primeira classe.')
print(instancia)
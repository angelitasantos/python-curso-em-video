'''
# Desafio 033

Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''


print('Digite três valores diferentes.')
valor_01 = int(input('Digite o primeiro valor: '))
valor_02 = int(input('Digite o segundo valor: '))
valor_03 = int(input('Digite o terceiro valor: '))

print('-' * 100)
# verificar qual o menor número
if valor_01 < valor_02 and valor_01 < valor_02:
    print(f'O MENOR valor digitado foi {valor_01}')
if valor_02 < valor_01 and valor_02 < valor_03:
    print(f'O MENOR valor digitado foi {valor_02}')
if valor_03 < valor_01 and valor_03 < valor_02:
    print(f'O MENOR valor digitado foi {valor_03}')

# verificar qual o maior número
if valor_01 > valor_02 and valor_01 > valor_02:
    print(f'O MAIOR valor digitado foi {valor_01}')
if valor_02 > valor_01 and valor_02 > valor_03:
    print(f'O MAIOR valor digitado foi {valor_02}')
if valor_03 > valor_01 and valor_03 > valor_02:
    print(f'O MAIOR valor digitado foi {valor_03}')

# verificar se os três números são iguais
if valor_01 == valor_02 == valor_03:
    print('Todos os números são iguais,')



# solução com listas

primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
numeros = [primeiro, segundo, terceiro]

menor = min(numeros)
maior = max(numeros)

print(f'O MAIOR número digitado foi {maior}.')
print(f'O MENOR número digitado foi {menor}.')




# solução com listas

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input ('Digite o terceiro número: '))

lista = [n1, n2, n3]
lista_ordenada = sorted(lista)

print(f'O MENOR número é {lista_ordenada[0]}.')
print (f'O MAIOR número é {lista_ordenada[2]}.')
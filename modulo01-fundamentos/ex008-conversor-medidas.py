'''
# Desafio 008

Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''


medida = float(input('Digite uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {km:.3f}km.')
print(f'A medida de {medida}m corresponde a {hm:.2f}hm.')
print(f'A medida de {medida}m corresponde a {dam:.1f}dam.')
print(f'A medida de {medida}m corresponde a {dm:.0f}dm.')
print(f'A medida de {medida}m corresponde a {cm:.0f}cm.')
print(f'A medida de {medida}m corresponde a {mm:.0f}mm.')
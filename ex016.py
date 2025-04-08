# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção Inteira.
numero = float(input('Digite um número: '))

print(f'A porção inteira de {numero} é {int(numero)}.')

# Ou ------------------------------------------------------------------
# from math import trunc

# numero = float(input('Digite um número: '))

# print(f'A porção inteira de {numero} é {trunc(numero)}.')

# Ou ------------------------------------------------------------------
# import math

# numero = float(input('Digite um número: '))

# print(f'A porção inteira de {numero} é {math.trunc(numero)}.')
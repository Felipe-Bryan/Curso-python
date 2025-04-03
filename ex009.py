# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um número: '))

print(f'A tabuada de {n} é:')

for i in range(1, 11):
    print(f'{n} x {i:2} = {n * i:2}')

print('Fim da tabuada')
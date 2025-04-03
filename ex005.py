# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro: '))
suc = n + 1
ant = n - 1
print(f'O sucessor de {n} é {suc} e o antecessor é {ant}.')

# ou

# print(f'O sucessor de {n} é {n + 1} e o antecessor é {n - 1}.')
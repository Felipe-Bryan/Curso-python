# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print(f'O dobro de {n} é {dobro}.\nO triplo de {n} é {triplo}.\nA raiz quadrada de {n} é {raiz:.2f}.')

# ou

# print(f'O dobro de {n} é {n * 2}.')
# print(f'O triplo de {n} é {n * 3}.')
# print(f'A raiz quadrada de {n} é {n ** (1/2):.2f}.')
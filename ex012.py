# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
desconto = 0.05
novo = preco - (preco * desconto)
print(f'O preço do produto com desconto de 5% é: R$ {novo:.2f}')

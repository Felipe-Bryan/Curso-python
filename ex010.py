# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dólares ela pode comprar.

# Considere a cotação do dólar a R$ 5,50.
valor = float(input('Quanto dinheiro você tem na carteira? R$ '))

dolar = 5.50

dolares = valor / dolar

print(f'Com R$ {valor:.2f} você pode comprar US$ {dolares:.2f}')
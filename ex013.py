# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e 
# mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$ '))
aumento = 0.15
novo_salario = salario + (salario * aumento)
print(f'O novo salário do funcionário com aumento de 15% é: R$ {novo_salario:.2f}')
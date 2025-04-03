# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite um valor: ')

print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'É alfanumérico? {valor.isalnum()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'É numérico? {valor.isnumeric()}')
print(f'É maiúsculo? {valor.isupper()}')
print(f'É minúsculo? {valor.islower()}')
print(f'É capitalizado? {valor.istitle()}')
print(f'É um espaço? {valor.isspace()}')
print(f'É um dígito? {valor.isdigit()}')
print(f'É um identificador? {valor.isidentifier()}')
print(f'É imprimível? {valor.isprintable()}')

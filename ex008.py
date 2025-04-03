# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Exemplo: 1m = 100cm = 1000mm

# Entrada de dados
metros = float(input('Digite um valor em metros: '))

print(f'{metros / 1000} km')
print(f'{metros / 100} hm')
print(f'{metros / 10} dam')
print(f'{metros} m')
print(f'{metros * 10} dm')
print(f'{metros * 100} cm')
print(f'{metros * 1000} mm')

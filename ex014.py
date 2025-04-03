# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em 
# graus Celsius e converta para graus Fahrenheit.

# Fórmula de conversão: F = C * 9/5 + 32

celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F!')

# Conversão inversa
# Fórmula de conversão: C = (F - 32) * 5/9

# fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))
# celsius = (fahrenheit - 32) * 5 / 9
# print(f'A temperatura de {fahrenheit}°F corresponde a {celsius}°C!')
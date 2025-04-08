# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do 
# seno, cosseno e tangente desse ângulo.

an = float(input('Digite o ângulo que você deseja: '))

from math import sin, cos, tan, radians

si = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, si))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, ta))
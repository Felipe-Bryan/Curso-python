# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

n= randint(1, 5)
print('-=--'*20)
print('Sou seu computador... Vou pensar em um número entre 1 e 5. Tente Adivinhá-lo!')
print('-=--'*20)
sleep(3)
n1= int(input('Pensei! Qual é o seu palpite? '))
if n1 == n:
    print('Você acertou!')
else:
    print(f'Você errou! O número que eu pensei foi {n}.')
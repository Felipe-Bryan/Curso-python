# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos 
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')

alunos = [al1, al2, al3, al4]
shuffle(alunos)

print('A ordem de apresentação será: ')
for i, aluno in enumerate(alunos, start=1):
    print(f'{i}º: {aluno}')


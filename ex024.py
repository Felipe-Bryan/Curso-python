# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela 
# começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da cidade? ')).strip()
print(f'A cidade começa com SANTO? {cidade[:5].upper() == 'SANTO'}')
# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Velocidade registrada: '))
if v > 80:
    print('Você foi multado!')
    m = (v - 80) * 7
    print(f'O valor da multa é de R${m:.2f}')

print('Tenha um bom dia, dirija com segurança!')
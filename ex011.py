# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = lg * alt
tinta = area / 2
print(f'Sua parede tem a dimensão de {lg} x {alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')
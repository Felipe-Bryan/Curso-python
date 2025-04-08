# Crie um programa que imprima "Olá Mundo!" na tela.
import emoji

print('*' * 30)
print(emoji.emojize('Olá Mundo! :globe_showing_Americas:'))
print('*' * 30)

print('{:-^30}'.format('Olá Mundo!'))  # Centralizado
print('{:-<30}'.format('Olá Mundo!'))  # Justificado à esquerda
print('{:->30}'.format('Olá Mundo!'))  # Justificado à direita

msg = 'Olá Mundo!'

print('*' * 30)
print(f'{msg :-^30}')
print('*' * 30)

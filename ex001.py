# Crie um programa que imprima "Olá Mundo!" na tela.

print('*' * 30)
print('Olá Mundo!')
print('*' * 30)

print('{:-^30}'.format('Olá Mundo!'))  # Centralizado
print('{:-<30}'.format('Olá Mundo!'))  # Justificado à esquerda
print('{:->30}'.format('Olá Mundo!'))  # Justificado à direita

msg = 'Olá Mundo!'

print('*' * 30)
print(f'{msg :-^30}')
print('*' * 30)

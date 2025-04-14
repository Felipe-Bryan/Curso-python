# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Dica: use o módulo pygame. Para instalar o módulo pygame, execute o comando: pip install pygame
import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3') # Indicar arquivo a ser executado
pygame.mixer.music.play()
pygame.event.wait()
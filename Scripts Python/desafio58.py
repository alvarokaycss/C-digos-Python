import pygame
from random import randint
from time import sleep
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('SuperMarioBros.mp3')
pygame.mixer.music.play()
print('VOU PENSAR EM UM NÚMERO DE [0 A 10] E VOCÊ TENTA ADVINHAR.')
print('PENSANDO EM UM NÚMERO...')
for c in range(5,0,-1):
    print(c)
    sleep(0.9)
print('JÁ PENSEI, AGORA TENTE ADIVINHAR!')
pc = randint(0, 10)
erro = 0
resposta = int(input('DIGITE UM NÚMERO:\n'))
while resposta != pc:
    erro += 1
    if resposta < pc: print('TENTE UM NÚMERO MAIOR!')
    else: print('TENTE UM NÚMERO MENOR!')
    resposta = int(input('VOCÊ ERROU! MAS VOU DEIXAR TENTAR NOVAMENTE:\n'))
pygame.mixer.music.stop()
print(f'PARABÉNS VOCÊ CONSEGUIU!!! E ERROU UM TOTAL DE {erro} VEZES.')
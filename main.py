import pygame
from time import sleep


campo = (100,100) # largura, comprimento
frutinhas = [(15,22),(89,68),(50,71),(11,85),(94,52)] # x , y

class snake:
    def __init__(self):
        self.tamanhoinicial = 1
        self.tamanho = self.tamanhoinicial
        self.cabeca = (50,50) # posição da cabeça
        self.distancia_da_parede = 50
        self.distancia_da_parede_direita = 30
        self.distancia_da_parede_esquerda = 30

    def se_move(self):
        entrada_do_usuario = input().lower()
        if entrada_do_usuario == 'w':
            self.distancia_da_parede -= 1

        if entrada_do_usuario == 'd':
            self.distancia_da_parede_direita -= 1
        
        elif entrada_do_usuario == 'e':
            self.distancia_da_parede_esquerda -= 1

    def come(self):
        if self.cabeca in frutinhas: 
            self.tamanho += 1
    
    def morre(self):
        if self.distancia_da_parede <= 0:
            self.tamanho = 0
            print('Você perdeu!!!')


cobra = snake()

while True:
    sleep(0.10)
    cobra.se_move()
    cobra.come()
    cobra.morre()
    print(cobra.distancia_da_parede)
    print(cobra.distancia_da_parede_direita)
    print(cobra.distancia_da_parede_esquerda)


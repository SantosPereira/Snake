import pygame, random
from pygame.locals import *
from autoplay import *


pygame.init()

print('\x1b[2J\x1b[1;1H')

def colisao (c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((100,255,90))

maca_pos = (random.randint(0,59)*10,random.randint(0,59)*10)
maca = pygame.Surface((10,10))
maca.fill((255,0,0))

direcao = LEFT
clock = pygame.time.Clock()

print('\033[1;31mPontuação:\033[;0m ')

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_RIGHT:
                direcao = RIGHT
            if event.key == K_LEFT:
                direcao = LEFT

    ### Autoplay ####
    direcao = autoplay(snake[0], maca_pos, direcao)
    #################

    if colisao(snake[0], maca_pos):
        maca_pos = (random.randint(0,59)*10,random.randint(0,59)*10)
        snake.append((0,0))
        pontuacao = len(snake)
        print('\x1b[2J\x1b[1;1H\033[1;31mPontuação:\033[;0m ', pontuacao)


    if snake[0][0] < 0 or snake[0][0] > 590 or snake[0][1] < 0 or snake[0][1] > 590: #morre na colisão com a parede
        print('morreu!')
        exit()

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))
    screen.blit(maca, maca_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)
    
    pygame.display.update()

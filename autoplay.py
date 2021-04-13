# snake[0] = x
# snake[1] = y

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def autoplay(snake, maca_pos, direcao):
    if abs(maca_pos[0] - snake[0]) < abs(maca_pos[1] - snake[1]) and abs(maca_pos[0] - snake[0]) > 0:
        if maca_pos[0] - snake[0] >= 1: # x
            direcao = RIGHT
            return direcao
        elif not maca_pos[0] - snake[0] >= 1:
            direcao = LEFT
            return direcao

    else:
        if maca_pos[1] - snake[1] >= 1:
            direcao = DOWN
            return direcao
        elif maca_pos[1] - snake[1] < 0:
            direcao = UP
            return direcao

            
        elif maca_pos[0] - snake[0] >= 1:
            direcao = RIGHT
            return direcao
        elif not maca_pos[0] - snake[0] >= 1:
            direcao = LEFT
            return direcao
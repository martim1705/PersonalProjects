import pygame as py 
import random as rndm


py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock() 

font = py.font.SysFont(None, 24)

spawn_rating = 1000 # em milissegundos! 

square = None
spawn_time = py.time.get_ticks()


player_points = 0 
running = True

# função para desenhar os quadrados 
def draw_square():
    return py.Rect(rndm.randint(50, 1230),rndm.randint(50, 680), 50, 50)

while running:
    currentTime = py.time.get_ticks()
    
    
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if square and square.collidepoint(pos):
                player_points += 1
                square = None

    
    
    screen.fill("white")


    if square is None:
        square = draw_square() 
        spawn_time = currentTime
    

    elif currentTime - spawn_time >= spawn_rating: 
        square = None

    if square: 
        py.draw.rect(screen, (0,0,0), square)
    
    score = font.render(f"Score: {player_points}", True, (0,0,0))
    screen.blit(score, (10,10))
       
    py.display.flip()
    clock.tick(60)

py.quit()
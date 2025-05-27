import pygame as py 
import random as rndm
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock() 
running = True

# função para desenhar os quadrados 
def draw_square():
    square = py.Rect(rndm.randint(50, 1230),rndm.randint(50, 680), 50, 50)
    py.draw.rect(screen, (0,0,0), square)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    
    screen.fill("white")

    draw_square()
    py.display.flip()
    clock.tick(60)

py.quit()
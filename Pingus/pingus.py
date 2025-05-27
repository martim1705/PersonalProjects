import pygame as py 
import random as rndm


py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock() 
# tamanho de 24, font qualquer 
font = py.font.SysFont(None, 40)

spawn_rating = 1000 # em milissegundos! 

square = None
spawn_time = py.time.get_ticks() # momento em que o quadrado aparece no ecrã 


player_points = 0 
running = True

# função para desenhar os quadrados 
def draw_square():
    return py.Rect(rndm.randint(50, 1230),rndm.randint(50, 680), 50, 50)

#enquanto o jogo corre
while running:
    #guarda o tempo atual
    currentTime = py.time.get_ticks()
    
    # para cada evento 
    for event in py.event.get():
        #se o jogador clicar no X, o programa fecha
        if event.type == py.QUIT:
            running = False
            #se o jogador clicar no botão direito do rato, guarda-se a posição do rato, e houver colisão soma-se um ponto ao score e põe square a None
        elif event.type == py.MOUSEBUTTONDOWN:
            pos = py.mouse.get_pos()
            if square and square.collidepoint(pos):
                player_points += 1
                square = None

    
    
    screen.fill("purple")


    if square is None:
        #se não houver quadrado desenha-se e atualiza-se o tempo em que o quadrado aparece para o momento atual
        square = draw_square() 
        spawn_time = currentTime
    

    elif currentTime - spawn_time >= spawn_rating: # se o quadrado estiver no ecrã à mais de 1 segundo, square = None
        square = None

    if square: # se o square != None, desenha-se no ecrã 
        py.draw.rect(screen, (0,0,0), square)
    #"Score: __ " aparece no ecrã 
    score = font.render(f"Score: {player_points}", True, (0,0,0))
    screen.blit(score, (20,20))
       
    py.display.flip()
    clock.tick(60)

py.quit()
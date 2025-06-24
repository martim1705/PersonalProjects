import pygame
from createObject import Object

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


#create Object 
object1 = Object(40, "blue", screen.get_width() / 2, screen.get_height() / 2)
object2 = Object(30, "purple", 450, 230)
currentObjects = [object1, object2]

#velocities 
velocities = {id(ball): 0.0 for ball in currentObjects}


gravity = 981         # aceleração da gravidade (px/s²)
energy_loss = 0.7071  # perda de ~50% da energia mecânica por rebote

dt = 0

while running:

    dt = clock.tick(60) / 1000


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    for ball in currentObjects:
        
        velY = velocities[id(ball)]

        radius = ball.getRadius()
        # Atualização da física
        velY += gravity * dt
        ball.posY += velY * dt

        # Colisão com o "chão"
        if ball.posY + radius >= 720:
            ball.posY = 720.0 - radius
            velY = -velY * energy_loss

            # Se a velocidade for muito pequena, parar
            if abs(velY) < 20:
                velY = 0

        pos = ball.pos()
        velocities[id(ball)] = velY
        # Desenho
        # Delta time
        
        pygame.draw.circle(screen, ball.getColor() ,pos , radius)
        
    pygame.display.flip()
    

pygame.quit()
import pygame
import sys

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Platform")

start_x, start_y = 400, 600
jumping = False
size = 20
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
FALL_VELOCITY = 0
floor = [[0, 620, 800, 10], [0, 540, 300, 10], [400, 360, 400, 10], [300, 280, 200, 10], [220, 570, 600, 10]]
on_floor = False
falling = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and falling == False:
        jumping = True
        

    if keys[pygame.K_a] and start_x > 0:
        start_x -= 5

    if keys[pygame.K_d] and start_x < 800 - size:
        start_x += 5
    
    for i in range (len(floor)):
        if ((floor[i][0] + floor[i][2]) >= start_x >= floor[i][0]) and ((floor[i][1] + floor[i][3] -  20) >= start_y >= floor[i][1] - 20):
            pass
        else:
            falling  = True
    

    if jumping:
        
        start_y -= Y_VELOCITY
        if(Y_VELOCITY > -10):
            Y_VELOCITY -= Y_GRAVITY

        for i in range (len(floor)):
            if ((floor[i][0] + floor[i][2]) >= start_x >= floor[i][0]) and ((floor[i][1] + floor[i][3]) >= start_y >= floor[i][1]):
                Y_VELOCITY = -1

            elif ((floor[i][0] + floor[i][2]) >= start_x >= floor[i][0]) and ((floor[i][1] + floor[i][3] -  20) >= start_y >= floor[i][1] - 20):
                on_floor = True
                start_y = floor[i][1] - 20

        if on_floor:
            on_floor = False
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
    
    elif falling:
            
            start_y -= FALL_VELOCITY
            if(FALL_VELOCITY > -10):
                FALL_VELOCITY -= Y_GRAVITY
            
            for i in range (len(floor)):
                if ((floor[i][0] + floor[i][2]) >= start_x >= floor[i][0]) and ((floor[i][1] + floor[i][3] -  20) >= start_y >= floor[i][1] - 20):
                        on_floor = True
                        start_y = floor[i][1] - 20

            if on_floor:
                on_floor = False
                falling = False
                FALL_VELOCITY = 0
            
    pygame.draw.rect(SCREEN, pygame.Color(0, 0, 0), (0, 0, 800, 800))
    pygame.draw.rect(SCREEN, pygame.Color(255, 255, 255), (start_x, start_y, size, size))
    for i in range (len(floor)):
        pygame.draw.rect(SCREEN, pygame.Color(255, 255, 255), floor[i])
    pygame.display.update()
    
    CLOCK.tick(60)


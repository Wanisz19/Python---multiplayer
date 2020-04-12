import pygame
import sys
import time
import snake


pygame.init()
width = 1200
heigh = 800
color = (150,0,0)
window = pygame.display.set_mode((width,heigh))
pygame.display.set_caption("Snake")
running = True
wonsz = snake.Snake(window,width,heigh)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if wonsz.direction !=2:
                    wonsz.direction = 1


            elif event.key == pygame.K_DOWN:
                if wonsz.direction !=1:
                    wonsz.direction = 2



            elif event.key == pygame.K_LEFT:
                if wonsz.direction !=4:
                    wonsz.direction = 3



            elif event.key == pygame.K_RIGHT:
                if wonsz.direction !=3:
                    wonsz.direction = 4



    wonsz.dirr()
    wonsz.rys()

    pygame.display.update()
    window.fill(color)




















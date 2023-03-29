import pygame
import numpy as np
import matplotlib.pyplot as plt

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
# creates main canvas
pygame.display.set_caption('a bit racey')
# adds title

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
# adds game clock for game time
carImg = pygame.image.load('newcar.png')




def car(x,y):
    gameDisplay.blit(carImg, (x,y))


pygame.transform.scale_by()



def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.5)
    x_change = 0

    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ie if window is closed
                gameExit = True
            print(event)
            # prints everything that's going on in the window,eg,moving mouse

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    x_change = 5
                    # pygame.transform.scale_by(pygame.image.load("newcar.png"),(2,1))
                elif event.key == pygame.K_a:
                    x_change = -5
            if event.type == pygame.KEYUP:
                x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
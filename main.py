import pygame
import numpy as np
import matplotlib.pyplot as plt

bg = pygame.image.load("bg.png")


pygame.init()

display_width = 920
display_height = 565

gameDisplay = pygame.display.set_mode((display_width,display_height))
# creates main canvas
pygame.display.set_caption('racing')
# adds title

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

clock = pygame.time.Clock()
# adds game clock for game time
carImg = pygame.image.load('newcar.png')

bg = pygame.image.load('bg.png')


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#pygame.transform.scale_by()



def game_loop():

    x =  (display_width * 0.45)
    y = (display_height * 0.5)
    x_change = 0

    l_track_edge = 200
    r_track_edge = 500

    moving_right = False
    moving_left = False

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
                    moving_right = True

                elif event.key == pygame.K_a:
                    moving_left = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    moving_right = False
                elif event.key == pygame.K_a:
                    moving_left = False


        if moving_right and x < r_track_edge:
            x_change = 5
            x += x_change
        elif moving_left and x > l_track_edge:
            x_change = -5
            x += x_change

        gameDisplay.fill(blue)

        gameDisplay.blit(bg, (0, 0))

        car(x, y)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
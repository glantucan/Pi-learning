#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
gameExit = False


# Initialize pygame
pygame.init()

# Setup the pygame canvas (called surface)
gameDisplay = pygame.display.set_mode((800, 600)) #The parameter is a tuple

pygame.display.set_caption('Slither')




# Game loop
while not gameExit:
    for event in pygame.event.get():
        # Setup exit conditions
        # See http://www.pygame.org/docs/ref/event.html for documentation on events
        if event.type == pygame.QUIT:
            gameExit = True 
    # Let's draw
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400, 300, 10, 100])
    pygame.draw.rect(gameDisplay, red, [400, 300, 10, 10])
    
    # Another method to draw rects which is in contrast to rect accelarated by the graphics card
    gameDisplay.fill(red, rect=[200, 200, 50, 50]) 
    #pygame.display.flip() # Updates the entire surface at once
    pygame.display.update() # Updates only what's needed   

pygame.quit() # Close pygame and cleanup

quit() # exit out of python
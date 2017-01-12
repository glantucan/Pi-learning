#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
gameExit = False
lead_x = 300
lead_y = 300

# Initialize pygame
pygame.init()

# Setup the pygame canvas (called surface)
gameDisplay = pygame.display.set_mode((800, 600)) # The parameter is a tuple
pygame.display.set_caption('Slither')

# Game loop
while not gameExit:
    for event in pygame.event.get():
        # Setup eevent conditions
        # See http://www.pygame.org/docs/ref/event.html for documentation on events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
            if event.key == pygame.K_UP:
                lead_y -= 10
            if event.key == pygame.K_DOWN:
                lead_y += 10

        
        if event.type == pygame.QUIT:
            gameExit = True 
    gameDisplay.fill(white)
    # Let's draw the head of the snake
    # pygame.draw.rect(gameDisplay, black, [400, 300, 10, 100])
    gameDisplay.fill(red, rect=[lead_x, lead_y, 10, 10]) 
    #pygame.display.flip() # Updates the entire surface at once
    pygame.display.update() # Updates only what's needed   

pygame.quit() # Close pygame and cleanup

quit() # exit out of python
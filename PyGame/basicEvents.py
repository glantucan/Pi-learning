#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame

# Initialize pygame

test = pygame.init()
print(test) # Should show the tuple (6, 0) Six succesess 0 failures initializing the pygame modules

# Setup the pygame canvas (called surface)

gameDisplay = pygame.display.set_mode((800, 600)) #The parameter is a tuple

pygame.display.set_caption('Slither')

#pygame.display.flip() # Updates the entire surface at once
pygame.display.update() # Updates only wht's needed

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        # See http://www.pygame.org/docs/ref/event.html for documentation
        if event.type == pygame.QUIT:
            gameExit = True 



pygame.quit() # Close pygame and cleanup

quit() # exit out of python
#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame

# Initialize pygame

test = pygame.init()

print(test)

# Setup the pygame canvas (called surface)

gameDisplay = pygame.display.set_mode((800, 600)) #The parameter is a tuple

#pygame.display.flip() # Updates the entire surface at once
pygame.display.update() # Updates only wht's needed

pygame.quit() # Close pygame and cleanup

quit() # exit out of python
#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame
import time
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)

surfaceWidth = 800
surfaceHeight = 600
blockSize = 10
gameExit = False
die = False
lead_x = 0
lead_y = 0
fps = 30 
speed = 0.2 #pixels/milisecond
clock = pygame.time.Clock()
x = surfaceWidth * 0.5
y = surfaceHeight * 0.5
# Initialize pygame
pygame.init()

# Setup the pygame canvas (called surface)
gameDisplay = pygame.display.set_mode((surfaceWidth, surfaceHeight)) # The parameter is a tuple
pygame.display.set_caption('Slither')

font = pygame.font.SysFont(None, 25)

# FUNCTION DEFINITIONS
def checkSelfKill(direction, value):
    global die
    if direction == -value:
        die = True

def renderMessage(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [surfaceWidth*.45, surfaceHeight*.2])


# Game loop
while not gameExit and not die:
    # There is also pygame.event.poll() which is probaly more efficient
    for event in pygame.event.get():
        # Setup event conditions
        # See http://www.pygame.org/docs/ref/event.html for documentation on events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                checkSelfKill(lead_x, -1)
                lead_x = -1
                lead_y = 0
            elif event.key == pygame.K_RIGHT:
                checkSelfKill(lead_x, 1)
                lead_x = 1
                lead_y = 0
            elif event.key == pygame.K_UP:
                checkSelfKill(lead_y, -1)
                lead_y = -1
                lead_x = 0
            elif event.key == pygame.K_DOWN:
                checkSelfKill(lead_y, 1)
                lead_y = 1
                lead_x = 0
        elif event.type == pygame.QUIT:
            gameExit = True 
    rawDisplacement = speed * clock.get_time()
    x += lead_x * rawDisplacement
    y += lead_y * rawDisplacement

    if x < 0 or x > surfaceWidth or y < 0 or y > surfaceHeight:
        gameExit = True
    
    gameDisplay.fill(white)
    # Let's draw the head of the snake
    # pygame.draw.rect(gameDisplay, black, [400, 300, 10, 100])
    gameDisplay.fill(red, rect=[x, y, blockSize, blockSize]) 
    #pygame.display.flip() # Updates the entire surface at once
    pygame.display.update() # Updates only what's needed   
    clock.tick(fps) # forces a sleep(1/30), sort of.
    #print (die)

renderMessage('GAME OVER', red)
pygame.display.update()
# Don't do this when using pygame (Why?)
time.sleep(2)
pygame.quit() # Close pygame and cleanup

quit() # exit out of python
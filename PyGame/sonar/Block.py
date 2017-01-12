#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import pygame
from colors import *

WALL = 1

class Block(pygame.sprite.Sprite):

    def __init__( self, parent, color = blue, width = 10, height = 10, position = (0, 0), type = WALL ):
        super(Block, self).__init__()
        self.image = pygame.Surface( (width, height))
        self.parent = parent
        
        self.color = color
        self.image.fill( color )
        
        self.alpha = 255
        self.image.set_alpha( self.alpha )
        self.parent.blit(self.image, (0, 0))
        self.rect = self.image.get_rect()
        self.type = type
        self.active = True
        self.set_position(position)

    def set_position( self, pos):
        self.rect = pos

    def update(self):
        #print(self.image.get_alpha())
        if self.alpha > 50:
            #print("--->",self.alpha)
            self.alpha -= 1
            self.image.set_alpha( self.alpha )
            self.parent.blit(self.image, self.rect)
        else:
            self.active = False
            '''self.image.set_alpha( 75 )
            self.parent.blit(self.image, self.rect)'''


if (__name__ == "__main__"):
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    window_size = (window_width, window_height) = (800, 800)
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    
    bgImg = pygame.image.load("imgs/sonar_bg_800x800_gauss.jpg")
    window.blit(bgImg, (0,0))

    block_group = pygame.sprite.Group()

    a_block = Block(window, green, 10, 10, (400, 300))
    block_group.add( a_block )
    # blit the group and its contents to the window (will be updated when the window updates)
    block_group.draw(window)


    running = True
    counter = 0
    while ( running ): 
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                running = False
        
        clock.tick(fps)
        
        window.blit(bgImg, (0,0))
        #a_block.update()
        block_group.update()
        
        pygame.display.update()
        counter += 1
    pygame.quit()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame
from math import tan, radians, fabs
from colors import *
from Block import Block

class RayCaster(object):
    def __init__(self, cellSize = (10, 10), worldSize = (100, 100), parent = None, group = None):
        """
        Initializes the ray caster setting the cellSize tuple and the worldSize tuple and creating the 2-dimensional array for 
        the cells.
        :param cellSize: A tuple describing the width and height of the cells we are dividing the world def main()
        :param worldSize: Another tuple describing the size of the world. Width and Height should be even multiples of the 
            corresponding cellSize width and height. 
        """
        self.__cellSize = cellSize
        self.__worldSize = worldSize
        self.__xCells =  worldSize[0] // cellSize[0] + 1 # Not doing so makes things asymetric
        self.__yCells =  worldSize[1] // cellSize[1] + 1
        self.__cells = [ [False] * self.__xCells ] * self.__yCells
        self.__surface = parent
        self.__group = group

    def rayCast(self, angle):
        angleNorm = self.__normalizeAngle(angle)
        if angleNorm != 90 and angleNorm != 270:
            if angleNorm < 90 or angleNorm > 270: 
                xMin = 1
                xMax = (self.__xCells - 1) // 2 + 1
                step = 1
            elif angleNorm > 90 and angleNorm < 270:
                xMin = -1
                xMax = -(self.__xCells - 1) // 2 - 1
                step = -1
            
            for cellX in range(xMin, xMax, step):
                cellY = self.__roundedY( tan(radians(angleNorm)) * cellX )
                
                #TODO: Need to fill the cells between y consecutive values
                
                xPos = (cellX + 40) * self.__cellSize[0]
                yPos = (cellY + 40) * self.__cellSize[1]

                newBlock = Block(self.__surface, green, 10, 10, (xPos, yPos))
                self.__group.add(newBlock)
                self.__group.draw(self.__surface)
    
    def __normalizeAngle(self, angle):
        if angle > 360 or angle < 360:
            angle = angle % 360
        if angle < 0:
            angle = 360 - angle
        return angle
    

    def __roundedY(self, y):
        return int(y//1 + 1)


if (__name__ == "__main__"):
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60

    window_size = (window_width, window_height) = (800, 800)
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    
    bgImg = pygame.image.load("imgs/sonar_bg_800x800_gauss.jpg")
    window.blit(bgImg, (0,0))
    
    ray_group = pygame.sprite.Group()
    ray_group.draw(window)

    rc = RayCaster((10, 10), (window_width, window_width), window, ray_group)
    curAngle = int(sys.argv[1])
    rc.rayCast(curAngle)


    running = True
    counter = 0
    while ( running ): 
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ):
                running = False
        
        clock.tick(fps)
        
        window.blit(bgImg, (0,0))
        #a_block.update()
        #block_group.update()
       
        if counter % 5 == 0:
            curAngle += 1
            rc.rayCast(curAngle)
        ray_group.update()
        pygame.display.update()
        counter += 1
    pygame.quit()
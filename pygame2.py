# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:52:02 2017

@author: DAKS
"""

import numpy as np
import random
import pygame


def show_square(full_square):
    global screen, sq_color
    GREEN = (0, 72, 0)
    #NEW = (random.randint(72,255), random.randint(72,255), random.randint(72,255))
    DARK = (96, 96, 96)
    
    for pos_y, data_y in enumerate(full_square):
        for pos_x, data_x in enumerate(data_y):
             
            x1 = pos_x * 5
            y1 = pos_y * 5
            x2 = x1 + 4
            y2 = y1 + 4
            rect = pygame.Rect((x1, y1), (x2, y2))
            image = pygame.Surface((4, 4))
            #NEW = (data_x*5, data_x*5, data_x*5)
            NEW = sq_color[int(data_x)]
            if (data_x==0):
                image.fill(GREEN)
            else:
                image.fill(NEW)
            screen.blit(image, rect)


def checking(sq):
    for si in sq:
        flag_checking = True
        for py in range(0,boxsize-si+1):
            for px in range(0,boxsize-si+1):
                cbox = mybox[py:py+si, px:px+si]
                if ((np.sum(cbox)==0) and flag_checking):
                    #print(py, px)
                    mybox[py:py+si, px:px+si].fill(si)
                    flag_checking = False
        if (flag_checking):
            break
        
    if (flag_checking):
        return False
    else:
        return True
    
#---------------------------------------------

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pygame.display.set_mode(((112*5)+1, (112*5)+1))
clock = pygame.time.Clock()
FPS = 30  # Frames per second.
BLACK = (0, 0, 0)


#mybox = np.random.randint(21, size=(112, 112))
boxsize = 112
mybox = np.zeros((boxsize, boxsize))
#sq = np.array([3,2,3])
sq = np.array([2,4,6,7,8,9,11,15,16,17,18,19,24,25,27,29,33,35,37,42,50])
sq_color = np.random.randint(255, size=(51, 3))

if (1):
    result = checking(sq)
    screen.fill(BLACK)
    show_square(mybox)
    pygame.display.flip()
        
#print(mybox)



running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and (
                        event.key == pygame.K_ESCAPE or 
                        event.key == pygame.K_q)):
            running = False
            pygame.quit()
            quit()

    #screen.fill(BLACK)
    #show_square(mybox)
    #pygame.display.flip()

from json import load
from turtle import speed
import pygame
from random import random
import time
import sys, pygame, pygame.mixer
from pygame.locals import * 
import math

pygame.init()

# zdefiniowane kolory
white = (255, 255, 255)
rosso=(255,0,0)
green = (0, 255, 0)
skyblue = (0,191,255)
black =(1,1,1)

X = 1200
Y = 700

display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Image')



while True:
    display_surface.fill(black)

    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit
                quit()



            pygame.display.update()




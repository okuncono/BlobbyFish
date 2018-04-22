#OTHER WEEKS USED TO UNDERSTAND FLAPPY BIRD CODE AND LEARN
#PROGRESS FROM LAST WEEK
#Marin worked on the spirites and design on the images.
#I worked on understanding the code and finding how to blit an image correctly with the sprite and background.
#I also learned how to bli an image onto a certian coordinate. 
#As well, I looked at the original flappy bird code and developed a feel for hwo the project should be made. 
#My teammate eliminated the problems and other stuff to creat our similar game to to flappy bird.

#EXAMPLE FROM CODE PYLET
import pygame
import pygame.gfxdraw
from pygame.locals import *
import sys
import os
from turtle import *
from random import randint

#Intialize settings and variables
pygame.init()
pygame.display.set_caption("Blobbyfish")
width = 600
wHalf = width / 2
height = 450
hHalf = height / 2
area = width * height
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 500
scroll = 0
mainGame = True

#Loading Images
#Background
background = pygame.image.load('FINAL PROJECT/images/finalbackground.png')
dimensions = background.get_rect()
print(dimensions)
#Blobfish
blobfish = pygame.image.load('FINAL PROJECT/images/finalblobfish.png')
blobfishDimen = blobfish.get_rect()
print(blobfishDimen)

#Functions
def eventFunction():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

def blobfishConfig():
    #Blitting blobfish on top of background
    screen.blit(blobfish, (375 - blobfishDimen.center[0], 375 - blobfishDimen.center[1]))

    #Turtle Control
    


def bombConfig():
    #Random bomb generated on screen

while mainGame == True:
    eventFunction()

    #Blitting images onto screen
    screen.blit(background, (wHalf - dimensions.center[0], hHalf - dimensions.center[1]))

    #Moving background infinitely
    repeatScroll = scroll % background.get_rect().width
    screen.blit(background, (repeatScroll - background.get_rect().width, 0))
    if repeatScroll < width:
        screen.blit(background, (repeatScroll, 0))
    scroll -= 1

    #Control and operation of blobfish sprite
    blobfishConfig()

    #Updates screen and frame rate
    pygame.display.update()
    clock.tick(FPS)
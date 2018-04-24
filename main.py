#OTHER WEEKS USED TO UNDERSTAND FLAPPY BIRD CODE AND LEARN
#PROGRESS FROM LAST WEEK
#Marin worked on the spirites and design on the images.
#I worked on understanding the code and finding how to blit an image correctly with the sprite and background.
#I also learned how to bli an image onto a certian coordinate. 
#As well, I looked at the original flappy bird code and developed a feel for hwo the project should be made. 
#My teammate eliminated the problems and other stuff to creat our similar game to to flappy bird.

#SOME CODE TAKEN FROM CODE PYLET'S TUTORIALS
import pygame
import pygame.gfxdraw
from pygame.locals import *
import sys
import os
from random import randint

#Intialize settings and variables
pygame.init()
pygame.display.set_caption("Blobbyfish")
    #Caption for game
width = 500
wHalf = width / 2
height = 500
hHalf = height / 2
area = width * height
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 500
scroll = 0
mainGame = True
keys = [False, False, False, False]
alive = 1

#Loading Images into Pygame
#Background
background = pygame.image.load('FINAL PROJECT/Blobbyfish/finalbackground.png')
dimensions = background.get_rect()
print(dimensions)
#Blobfish
blobfish = pygame.image.load('FINAL PROJECT/Blobbyfish/blobfishfinal.png')
blobfishDimen = blobfish.get_rect()
blobfishPos = [375 - blobfishDimen.center[0], 375 - blobfishDimen.center[1]]
print(blobfishDimen)

#Functions
def eventFunction():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

def blobfishConfig():
    #Blitting blobfish on top of background
    screen.blit(blobfish, blobfishPos)

    #Control of Blobfish - TAKEN FROM https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #In the event, if the key that is pushed down is either w, a, s, or d, it will state true for that certain key.
                if event.key==K_w:
                    keys[0]=True
                elif event.key==K_a:
                    keys[1]=True
                elif event.key==K_s:
                    keys[2]=True
                elif event.key==K_d:
                    keys[3]=True
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    keys[0]=False
                elif event.key==pygame.K_a:
                    keys[1]=False
                elif event.key==pygame.K_s:
                    keys[2]=False
                elif event.key==pygame.K_d:
                    keys[3]=False
        if keys[0]:
            blobfishPos[1]-=5
            #The position is subtracted from blobfishPos. 
            #The pixels decrease the higher up the character goes. It increases the lower it goes
        elif keys[2]:
            blobfishPos[1]+=5
        if keys[1]:
            blobfishPos[0]-=5
            #The pixels decrease as the character goes left. It increases as the character goes right.
        elif keys[3]:
            blobfishPos[0]+=5



#def bombConfig():
    #Random bomb generated on screen

#Main loop
while mainGame == True:
    eventFunction()
    #Blitting images onto screen
    screen.blit(background, (wHalf - dimensions.center[0], hHalf - dimensions.center[1]))

    #Moving background infinitely
    #CODE TAKEN FROM YOUTUBER "Code Pylet"
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

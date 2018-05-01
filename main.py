#OTHER WEEKS USED TO UNDERSTAND FLAPPY BIRD CODE AND LEARN
#PROGRESS FROM LAST WEEK
#Marin worked on the spirites and design on the images.
#I worked on understanding the code and finding how to blit an image correctly with the sprite and background.
#I also learned how to bli an image onto a certian coordinate. 
#As well, I looked at the original flappy bird code and developed a feel for hwo the project should be made. 
#My teammate eliminated the problems and other stuff to creat our similar game to to flappy bird.

import os
import sys
from random import randint

#SOME CODE TAKEN FROM CODE PYLET'S TUTORIALS
import pygame
import pygame.gfxdraw
from pygame.locals import *

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
FPS = 1000
scroll = 0
mainGame = True
keys = [False, False, False, False]
alive = 1
movement = [True, True, True, True]

#Loading Images into Pygame
#Background
background = pygame.image.load('FINAL PROJECT/Blobbyfish/finalbackground.png')
dimensions = background.get_rect()
print(dimensions)
#Blobfish
blobfish = pygame.image.load('FINAL PROJECT/Blobbyfish/blobfishfinal.png')
blobfishDimen = blobfish.get_rect()
blobfishPos = [0, 250]
print(blobfishDimen)
#Bomb
bombTop = pygame.image.load('FINAL PROJECT/Blobbyfish/bomb0.png')
bombMid = pygame.image.load('FINAL PROJECT/Blobbyfish/bomb1.png')
bombBot = pygame.image.load('FINAL PROJECT/Blobbyfish/bomb2.png')
#bombDimen = bomb.get_rect()
bombPosTop = [500, 105]
bombPosMid = [500, 205]
bombPosBot = [500, 305]
bombTopAlive = False
bombMidAlive = False
bombBotAlive = False

#Functions
def eventFunction():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#Booleans defining when to move bombs across the screen
def checkPos():
    if bombPosTop[0] <= -90:
        bombPosTop[0] += 590
        bombTopAlive = False
    if bombPosMid[0] <= -90:
        bombPosMid[0] += 590
        bombMidAlive = False
    if bombPosBot[0] <= -90:
        bombPosBot[0] += 590
        bombBotAlive = False

#Bomb Configuration
def randomBombGen():
    amountBomb = randint(1,3)
    #array = ["top", "middle", "bottom"]
    resultArray1 = randint(2, 3)
    resultArray2 = randint(2, 3)
    resultArray = randint(1, 3)
    resultArray3 = randint(1,2)
    if amountBomb == 1:
        if resultArray == 1:
            bombTopAlive = True
        if resultArray == 2:
            bombMidAlive = True
        if resultArray == 3:
            bombBotAlive = True
    # if amountBomb == 2:
    #     if resultArray == 1:
    #         screen.blit(bombTop, bombPosTop)
    #         if resultArray1 == 2:
    #             screen.blit(bombMid, bombPosMid)
    #             bombAlive = True
    #         if resultArray1 == 3:
    #             screen.blit(bombBot, bombPosBot)
    #             bombAlive = True
    #     if resultArray == 2:
    #         screen.blit(bombMid, bombPosMid)
    #         if resultArray2 == 2:
    #             screen.blit(bombTop, bombPosTop)
    #             bombAlive = True
    #         if resultArray2 == 3:
    #             screen.blit(bombBot, bombPosBot)
    #             bombAlive = True
    #     if resultArray == 3:
    #         screen.blit(bombBot, bombPosBot)
    #         if resultArray3 == 1:
    #             screen.blit(bombTop, bombPosTop)
    #             bombAlive = True 
    #         if resultArray3 == 2:
    #             screen.blit(bombMid, bombPosMid)
    #             bombAlive = True
    # if amountBomb == 3:
    #     screen.blit(bombTop, bombPosTop)
    #     screen.blit(bombMid, bombPosMid)
    #     screen.blit(bombBot, bombPosBot)
    #     bombAlive = True
    

################# M A I N   L O O P #################

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
    scroll -= 2

    #Configurating bomb movement in the loop
    screen.blit(bombTop, bombPosTop)
    screen.blit(bombMid, bombPosMid)
    screen.blit(bombBot, bombPosBot)
    checkPos()
    if bombPosTop[0] == 500:
        randomBombGen()
    if bombPosMid[0] == 500:
        randomBombGen()
    if bombPosBot[0] == 500:
        randomBombGen()
    if bombTopAlive == True:
        bombPosTop[0] -= 5
    if bombMidAlive == True:
        bombPosMid[0] -= 5
    if bombBotAlive == True:
        bombPosBot[0] -= 5
    
    #Configurating controls for blobfish
    screen.blit(blobfish, blobfishPos)

    #Collision Config blobfish and pygame window
    #Setting Collision Boundaries for sprite.
    #Used math and dimensions of the sprite to calculate the certain pixel points where it would stop.
    if blobfishPos[0] == 420:
        movement[3] = False
    elif blobfishPos[0] != 420:
        movement[3] = True
    if blobfishPos[0] == 0:
        movement[1] = False
    elif blobfishPos[0] != 0:
        movement[1] = True
    if blobfishPos[1] == 450:
        movement[2] = False
    elif blobfishPos[1] != 450:
        movement[2] = True
    if blobfishPos[1] == 0:
        movement[0] = False
    elif blobfishPos[1] != 0:
        movement[0] = True

#Width 80
#Heigt 50

    #Controling movement of blobfish
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
    if keys[0] == True and movement[0] == True:
        blobfishPos[1]-=5
        #The position is subtracted from blobfishPos. 
        #The pixels decrease the higher up the character goes. It increases the lower it goes
    elif keys[2] == True and movement[2] == True:
        blobfishPos[1]+=5
    if keys[1] == True and movement[1] == True:
        blobfishPos[0]-=5
        #The pixels decrease as the character goes left. It increases as the character goes right.
    elif keys[3] == True and movement[3] == True:
        blobfishPos[0]+=5
        scroll -=4

    #Updates screen and frame rate
    pygame.display.update()
    clock.tick(FPS)

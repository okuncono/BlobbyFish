#PROGRESS FROM WEEK
#Marin worked on the spirites and design on the images. He also worked on displaying the image.
#Teddy worked on understanding the code and finding how to blit an image correctly with the sprite and background.
#Teddy also learned how to bli an image onto a certian coordinate. 
#As well, Teddy looked at the original flappy bird code and developed a feel for hwo the project should be made. 
#My teammate eliminated the problems and other stuff to creat our similar game to to flappy bird.

#EXAMPLE FROM CODE PYLET
import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

#Display Setup
screenWidth = 750
screenHeight = 750
widthHalf = screenWidth / 2
heightHalf = screenHeight / 2
screenArea = screenWidth * screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Load Images
background = pygame.image.load('FINAL PROJECT/background.png')
dimensions = background.get_rect()
print(dimensions)
sprite = pygame.image.load('FINAL PROJECT/blobfish-jump.png')
spriteDimen = sprite.get_rect()
print(spriteDimen)

#Functions?
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == ESCAPE):
            pygame.quit()
            sys.exit()

#Loop
while True:
    event_handler()

    screen.blit(background, (widthHalf - dimensions.center[0], heightHalf - dimensions.center[1]))
    screen.blit(sprite, (375 - spriteDimen.center[0], 375 - spriteDimen.center[1]))
    pygame.display.update()


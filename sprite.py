import pygame
import pygame.gfxdraw
from pygame.locals import *

class Fish():
    def __init__(self, position, oxygen, points):
        self.position = position
        self.oxygen = oxygen
        self.points = points
    def checkFishLayer(self, position):
        global blobfish
        if position[1] <= 75:
            blobfish = pygame.image.load('blobfishfinalhalo.png')
        elif position[1] >= 375:
            blobfish = pygame.image.load('blobfishfinalmud.png')
        else:
            blobfish = pygame.image.load('blobfishfinal.png')

    

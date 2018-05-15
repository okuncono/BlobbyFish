#Here are the imports to run the game: os and system to run the program. Random for different random generators.
    #I imported the class fish from the file sprite inside the folder. It was overall a display of my use of classes in different files.
    #I also imported time (sleep function), and other pygame functions for the game itself.
import os, sys
from random import randint
from sprite import Fish
from time import sleep
import pygame
import pygame.gfxdraw
from pygame.locals import *

#################################################################################################################

#Here is a list of the different variables used within the game. As well, the game intialized here.
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Blobbyfish")
    #Caption for game
width = 500
wHalf = width / 2
height = 500
hHalf = height / 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 1000
scroll = 0
mainGame = True
keys = [False, False, False, False]
movement = [True, True, True, True]
    #This is used for movement. It is booleans that allow the blobfish to move depending on the boolean value.
alive = 1
pointsCounted = False
gameStart = False
black = (0,0,0)
white = (255, 255, 255)

#Loading Images into Pygame and other variables for the game
#Background
background = pygame.image.load('finalbackground.png')
backgroundRect = background.get_rect()
#Bomb
#TOP
bombTop = pygame.image.load('bomb0.png')
global bombTopDimen
bombTopDimen = bombTop.get_rect()
bombMaskTop = pygame.mask.from_surface(bombTop)
bombPosTop = [500, 105]
bombTopAlive = False
bombCenterTop = [bombPosTop[0] + bombTopDimen.center[0], bombPosTop[1]]
    #Here the bomb is loaded into pygame and its rect is calculated. Other values are used for positioning, collisions, and etc.
#MID
bombMid = pygame.image.load('bomb1.png')
global bombMidDimen
bombMidDimen = bombMid.get_rect()
bombMaskMid = pygame.mask.from_surface(bombMid)
bombPosMid = [500, 205]
bombMidAlive = False
bombCenterMid = [bombPosMid[0] + bombMidDimen.center[0], bombPosMid[1]]
#BOT
bombBot = pygame.image.load('bomb2.png')
global bombBotDimen
bombBotDimen = bombBot.get_rect()
bombMaskBot = pygame.mask.from_surface(bombBot)
bombPosBot = [500, 305]
bombBotAlive = False
bombCenterBot = [bombPosBot[0] + bombBotDimen.center[0], bombPosBot[1]]
#Here different images and other variables and values are used for the fucntioning of the blobfish.
blobfish = pygame.image.load('blobfishfinal.png')
blobfishDimen = blobfish.get_rect()
blobfishMask = pygame.mask.from_surface(blobfish)
mud = False
air = False
water = False
blobfishClass = Fish([0, 250], 150, 0)
    # ^^^ Here, the fish class from the sprites file is imported with a blobfish being the class. The different parameters are within the parentheses.
#Menu and gameover images are loaded into pygame
menu = pygame.image.load('menu.png')
gameover = pygame.image.load('gameover.png')

#Here are the images for the numbers loaded into pygame.
global numbers
numbers = (
    pygame.image.load('0.png'),
    pygame.image.load('1.png'),
    pygame.image.load('2.png'),
    pygame.image.load('3.png'),
    pygame.image.load('4.png'),
    pygame.image.load('5.png'),
    pygame.image.load('6.png'),
    pygame.image.load('7.png'),
    pygame.image.load('8.png'),
    pygame.image.load('9.png')
)
#Music from Nintendo
pygame.mixer.music.load("mariounderwatertheme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(15)

#################################################################################################################
#Here are the different functions used within the game.
#This function checks the position of the bomb to see if it is fully past the screen. Once the entire image is fof the screen, it is reset to the otehr side of the screen to run across the background as standstill bombs.
def checkBombPos():
    global pointsCounted
    if bombPosTop[0] <= -90:
        #The x value -90 is when all the bom's pixels are off the screen.
        #As well, it lets the program know that the points have not been counted for this next wave and it lets the program know that the bombs are not moving across the screen.
        bombPosTop[0] = 500
        bombCenterTop[0] = 545
        global bombTopAlive
        bombTopAlive = False
        pointsCounted = False
    if bombPosMid[0] <= -90:
        bombPosMid[0] = 500
        global bombMidAlive
        bombMidAlive = False
        pointsCounted = False
    if bombPosBot[0] <= -90:
        bombPosBot[0] = 500
        global bombBotAlive
        bombBotAlive = False
        pointsCounted = False

#This function checks if the game collides with any of the bombs.
def checkDead():
    #CODE TAKEN FROM CODE PYLET
    #This code takes the offset of the blobfish's position and the bomb's position. if the offset reaches a certain value within the mask of the blobfish, it recognizes it as a collision. It is registered as a boolean.
    global gameStart
    offset = [(blobfishClass.position[0] - bombCenterTop[0], blobfishClass.position[1] - bombCenterTop[1]), (blobfishClass.position[0] - bombCenterMid[0], blobfishClass.position[1] - bombCenterMid[1]), (blobfishClass.position[0] - bombCenterBot[0], blobfishClass.position[1] - bombCenterBot[1])]
    offset1 = [(blobfishClass.position[0] - bombPosTop[0], blobfishClass.position[1] - bombPosTop[1]), (blobfishClass.position[0] - bombPosMid[0], blobfishClass.position[1] - bombPosMid[1]), (blobfishClass.position[0] - bombPosBot[0], blobfishClass.position[1] - bombPosBot[1])]
    collisionTop, collisionTop1 = bombMaskTop.overlap(blobfishMask, offset[0]), bombMaskTop.overlap(blobfishMask, offset1[0])
    collisionMid, collisionMid1 = bombMaskMid.overlap(blobfishMask, offset[1]), bombMaskMid.overlap(blobfishMask, offset1[1])
    collisionBot, collisionBot1 = bombMaskBot.overlap(blobfishMask, offset[2]), bombMaskBot.overlap(blobfishMask, offset1[2])
    if collisionTop or collisionTop1 or collisionMid or collisionMid1 or collisionBot or collisionBot1 or blobfishClass.oxygen == 0:
        #If a collision occurs or oxygen runs out, it will blit a standstill background and gameover logo. It will update the screen and sleep so the gameover screen appears for only 2 seconds.
        #After this, it will set the game start to false and the game restarts all over.
        screen.blit(background, (0,0))
        screen.blit(gameover, (0,0))
        showScore(blobfishClass.points)
        pygame.display.update()
        sleep(2)
        gameStart = False

#This function basically draws the oxygen bar at the bottom left of the screen.
def oxygenBar(surface, x, y, startingOxygen, oxygen):
    #Code taken from Mr. Cozort. The bar here basically displays how much oxygen the fish has left before it dies.
    #It basically draws the bar based off the value of the oxygen I set (which is 150). This should set the bar to be 150 pixels long.
    if oxygen < 0:
        oxygen = 0
    oxyBarLength = startingOxygen
    oxyBarHeight = 20
    fill = (oxygen / 100) * 100
    outlineRect = pygame.Rect(x, y, oxyBarLength, oxyBarHeight)
    fillRect = pygame.Rect(x, y, fill, oxyBarHeight)
    pygame.draw.rect(surface, white, fillRect)
    pygame.draw.rect(surface, black, outlineRect, 2)

#This function displays the a combination of the numbers to display how many points you have.
def showScore(points):
    #TAKEN FROM FLAPPY BIRD CODE
    scoreDigits = [int(x) for x in list(str(points))]
    totalWidth = 0 
    #The total width of all numbers to be printed
    for digit in scoreDigits:
        totalWidth += numbers[digit].get_width()
    #Takes the width of all the images and finds the total width and divides it by 2 to find the center. It blits the center accordingly.
    Xoffset = (width - totalWidth) / 2
    for digit in scoreDigits:
        screen.blit(numbers[digit], (Xoffset, 10))
        Xoffset += numbers[digit].get_width()

#This function randomly generates a bomb accordingly.
def randomBombGen():
    global amountBomb
    if blobfishClass.points > 75:
        amountBomb = randint(4,6)
    else:
        amountBomb = randint(1,6)
        #This changes the difficulty based on how many points the user has.
    #array = ["top", "middle", "bottom"]
    resultArray1 = randint(2, 3)
    resultArray2 = randint(2, 3)
    resultArray = randint(1, 3)
    resultArray3 = randint(1,2)
    global bombTopAlive
    global bombMidAlive
    global bombBotAlive
    if amountBomb == 1 or amountBomb == 2:
        if resultArray == 1:
            bombTopAlive = True
            #If the bomb is alive, it is automatically moved across the screen in the main loop.
        if resultArray == 2:
            bombMidAlive = True
        if resultArray == 3:    
            bombBotAlive = True
    if amountBomb == 3 or amountBomb == 4 or amountBomb == 5:
        if resultArray == 1:
            bombTopAlive = True
            if resultArray1 == 2:
                bombMidAlive = True
            if resultArray1 == 3:
                bombBotAlive = True
        if resultArray == 2:
            bombMidAlive = True
            if resultArray2 == 2:
                bombTopAlive = True
            if resultArray2 == 3:
                bombBotAlive = True
        if resultArray == 3:
            bombBotAlive = True
            if resultArray3 == 1:
                bombTopAlive = True
            if resultArray3 == 2:
                bombMidAlive = True
    if amountBomb == 6:
        bombTopAlive = True
        bombMidAlive = True
        bombBotAlive = True
    #All of this represents the different bomb combos there are.

#This function  basically resets the game back to original settings once the fish dies.
def reset():
    if gameStart == False:
        global points
        blobfishClass.points = 0
        blobfishClass.position = [0, 225]
        bombPosTop[0] = 500
        bombPosMid[0] = 500
        bombPosBot[0] = 500
        blobfishClass.oxygen = 150

#################################################################################################################

################# M A I N   L O O P #################

while mainGame == True:
    #Blitting images onto screen
    screen.blit(background, (wHalf - backgroundRect.center[0], hHalf - backgroundRect.center[1]))
    repeatScroll = scroll % background.get_rect().width
    screen.blit(background, (repeatScroll - background.get_rect().width, 0))
    if repeatScroll < width:
        screen.blit(background, (repeatScroll, 0))
    scroll -= 10
        #This basically scrolls the background infinetly as long as the loop is still functioning.
        #CODE TAKEN FROM YOUTUBER "Code Pylet"
    
    #Blitting the blobfish
    blobfishState = blobfishClass.checkFishLayer(blobfishClass.position)
    screen.blit(blobfishState, blobfishClass.position)
    
    #Configurating bomb movement in the loop. It includes blitting the image and checking if the bomb is alive. If it is alive through the random bomb gen, it should move across the screen.
    screen.blit(bombTop, bombPosTop)
    screen.blit(bombMid, bombPosMid)
    screen.blit(bombBot, bombPosBot)
    if bombTopAlive == True:
        bombPosTop[0] -= 10
    if bombMidAlive == True:
        bombPosMid[0] -= 10
    if bombBotAlive == True:
        bombPosBot[0] -= 10
    checkBombPos()
    if bombPosTop[0] == 500 and bombPosMid[0] == 500 and bombPosBot[0] == 500 and gameStart == True:
        randomBombGen()

    #Checking score based off how many waves go by
    #If the x position of the blobfish is past the x position of the bomb, it will count how many bombs pass by and add that amount to points.
    if pointsCounted == False:
        if bombPosTop[0] < blobfishClass.position[0] or bombPosMid[0] < blobfishClass.position[0] or bombPosTop[0] < blobfishClass.position[0]:
            if blobfishClass.position[1] <= 75:
                blobfishClass.oxygen -= 30
            if blobfishClass.position[1] >= 375:
                blobfishClass.oxygen -= 30
            if blobfishClass.position[1] < 375 and blobfishClass.position[1] > 75:
                if blobfishClass.oxygen < 150:
                    blobfishClass.oxygen += 15
                    #This part checks to see if the blobfish is in the sand or air. If it is, it takes away oxygen. if it is in water, it adds oxygen unless it is already at full capacity.
                    #It adds or removes oxygen after every bomb wave passes the position of the blobfish.
            blobfishClass.points += 1
            pointsCounted = True

    #Collision Config blobfish and pygame window
    #Setting Collision Boundaries for sprite.
    #Used math and dimensions of the sprite to calculate the certain pixel points where it would stop.
    if blobfishClass.position[0] >= 420:
        movement[3] = False
    elif blobfishClass.position[0] != 420:
        movement[3] = True
    if blobfishClass.position[0] <= 0:
        movement[1] = False
    elif blobfishClass.position[0] != 0:
        movement[1] = True
    if blobfishClass.position[1] >= 450:
        movement[2] = False
    elif blobfishClass.position[1] != 450:
        movement[2] = True
    if blobfishClass.position[1] <= 0:
        movement[0] = False
    elif blobfishClass.position[1] != 0:
        movement[0] = True

    #Collision with Bombs, showing the score by displaying the points, resetting the game if there is a collision, blitting the menu and running the oxygen meter.
    checkDead()
    if gameStart == True:
        showScore(blobfishClass.points)
    reset()
    if gameStart == False:
        screen.blit(menu, (0,0))
    oxygenBar(screen, 10, 410, 150, blobfishClass.oxygen)

    #Controling movement of blobfish (same from bunny game)
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                gameStart = True
                #In the event, if the key that is pushed down is either w, a, s, or d, it will state true for that certain key.
                if event.key==K_ESCAPE:
                    quit()
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
        blobfishClass.position[1]-=10
        #The position is subtracted from blobfishClass.position. 
        #The pixels decrease the higher up the character goes. It increases the lower it goes
    elif keys[2] == True and movement[2] == True:
        blobfishClass.position[1]+=10
    if keys[1] == True and movement[1] == True:
        blobfishClass.position[0]-=10
        #The pixels decrease as the character goes left. It increases as the character goes right.
    elif keys[3] == True and movement[3] == True:
        blobfishClass.position[0]+=10

    #Updates screen and sets frame rate
    pygame.display.update()
    clock.tick(FPS)

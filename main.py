import pygame
import random
#initialize
pygame.init()
#create screen
screen = pygame.display.set_mode((800, 600))

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('star-wars.png')
playerX = 350
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y))

#enemy
enemyImg = pygame.image.load('star-wars.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0
enemyY_change = 0
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#game loop
running = True
while running:
    #take inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.5
            if event.key == pygame.K_UP:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN:
                playerY_change = +0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP:
                playerY_change = 0
            if event.key == pygame.K_DOWN:
                playerY_change = 0

                


    #set screen color (rgb)
    screen.fill((255, 255, 255))

    #draw player
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 738:
        playerX = 738
    if playerY <= 0:
        playerY = 0
    elif playerY >= 534:
        playerY = 534
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    #update screen
    pygame.display.update()
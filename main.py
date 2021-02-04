import pygame
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
playerX = 370
playerY = 480
def player(x, y):
    screen.blit(playerImg, (x, y))

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
                


    #set screen color (rgb)
    screen.fill((255, 255, 255))
    player(playerX, playerY)

    #update screen
    pygame.display.update()
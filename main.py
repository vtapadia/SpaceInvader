import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Space Invader")

icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 400
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load("spaceship.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def xBound(x):
    if x <= 0:
        x = 0
    elif x >= 760:
        x = 760
    return x

running = True
while running:
    screen.fill((210, 214, 214))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    playerX += playerX_change
    # Checking for boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 760:
        enemyX_change = -0.3
        enemyY += enemyY_change

    enemyX += enemyX_change
    # playerY += playerY_change
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()


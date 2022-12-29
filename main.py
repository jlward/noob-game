import random

import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Title and icon
pygame.display.set_caption('Noob Game')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0
player_y_change = 0

speed = 4

# Enemy
enemy_image = pygame.image.load('alien.png')
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 3
enemy_y_change = 40


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y):
    screen.blit(enemy_image, (x, y))


# Game Loop
running = True
while running:
    # RGB - (Red, Green, Blue)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check weather it's right or left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1 * speed
            if event.key == pygame.K_RIGHT:
                player_x_change = speed
            if event.key == pygame.K_UP:
                player_y_change = -1 * speed
            if event.key == pygame.K_DOWN:
                player_y_change = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    player_x += player_x_change
    player_y += player_y_change

    if player_x < 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    if player_y < 0:
        player_y = 0
    elif player_y >= 536:
        player_y = 536

    enemy_x += enemy_x_change
    if enemy_x < 0:
        enemy_x_change = enemy_x_change * -1
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = enemy_x_change * -1
        enemy_y += enemy_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()

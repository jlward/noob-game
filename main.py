import math
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
class Enemy:
    def __init__(self):
        self.enemy_image = pygame.image.load('alien.png')
        self.enemy_x_change = 3
        self.enemy_y_change = 40
        self.respawn()

    def respawn(self):
        self.enemy_x = random.randint(0, 700)
        self.enemy_y = random.randint(50, 150)


num_enemies = 6
enemies = []
for _ in range(6):
    enemies.append(Enemy())


bullet_image = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 0
bullet_y_change = 10
bullet_state = 'ready'


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10


def player(x, y):
    screen.blit(player_image, (x, y))


def draw_enemy(enemy):
    screen.blit(enemy.enemy_image, (enemy.enemy_x, enemy.enemy_y))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(
        math.pow((enemy_x - bullet_x), 2) + math.pow((enemy_y - bullet_y), 2),
    )
    if distance < 27:
        return True
    return False


def fire_bullet(x, y):
    global bullet_state  # WHY GLOBAL. Lol
    bullet_state = 'fire'
    screen.blit(bullet_image, (x + 16, y + 10))


def show_score(x, y):
    rendered_score = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(rendered_score, (x, y))


# Game Loop
running = True
while running:  # noqa
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
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_x = player_x
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)
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

    for enemy in enemies:
        enemy.enemy_x += enemy.enemy_x_change
        if enemy.enemy_x < 0:
            enemy.enemy_x_change = enemy.enemy_x_change * -1
            enemy.enemy_y += enemy.enemy_y_change
        elif enemy.enemy_x >= 736:
            enemy.enemy_x_change = enemy.enemy_x_change * -1
            enemy.enemy_y += enemy.enemy_y_change

    if bullet_state == 'fire':
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
    if bullet_y < 0:
        bullet_state = 'ready'

    # Collision
    for enemy in enemies:
        collision = is_collision(enemy.enemy_x, enemy.enemy_y, bullet_x, bullet_y)
        if collision:
            bullet_state = 'ready'
            score += 1
            enemy.respawn()

    player(player_x, player_y)
    for enemy in enemies:
        draw_enemy(enemy)
    show_score(text_x, text_y)
    pygame.display.update()

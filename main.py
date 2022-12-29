import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Noob Game')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
player_image = pygame.image.load('player.png')
player_x = 370
player_y = 480


def player():
    screen.blit(player_image, (player_x, player_y))


# Game Loop
running = True
while running:
    # RGB - (Red, Green, Blue)
    screen.fill((255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()

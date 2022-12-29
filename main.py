import pygame

pygame.init()


screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Noob Game')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 0))
    pygame.display.update()

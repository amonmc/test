# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
playerColor = (255, 0, 0)


playerRect = pygame.Rect(50, 50, 100, 100)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_w):
                playerRect.y -= 10
            if (event.key == pygame.K_s):
                playerRect.y += 10
            if (event.key == pygame.K_d):
                playerRect.x += 10
            if (event.key == pygame.K_a):
                playerRect.x -= 10

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE


    

    pygame.draw.rect(screen, playerColor, playerRect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
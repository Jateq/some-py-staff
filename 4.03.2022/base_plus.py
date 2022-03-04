import pygame
pygame.init() #main thing
# Global Variables
WIDTH = 800
HEIGTH = 600
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGTH)) #X AND Y
pygame.display.set_caption('Valorant')

finished = False
FPS = 20
clock = pygame.time.Clock()
move = 0
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (WIDTH//4, (HEIGTH//2 + move) % HEIGTH), (WIDTH * 3 // 4, ((HEIGTH//2 + move) % HEIGTH)), 10)
    move +=5
    pygame.display.flip()

pygame.quit()
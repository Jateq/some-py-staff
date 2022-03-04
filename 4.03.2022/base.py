import pygame
pygame.init() #main thing
# Global Variables
WIDTH = 800
HEIGTH = 600

screen = pygame.display.set_mode((WIDTH, HEIGTH)) #X AND Y
pygame.display.set_caption('Valorant')

finished = False
FPS = 20
clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    pygame.display.flip()

pygame.quit()
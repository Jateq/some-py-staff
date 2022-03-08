# movement
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Valorant')
clock = pygame.time.Clock()
finished = False
x, y = 0, 0
dx, dy = 5, 5
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (x, y, 120, 80))        
    x += dx
    y += dy
    if x + 120 >= WIDTH or x == 0:
        dx *= -1
    
    if y + 80 >= HEIGHT or y == 0:
        dy *= -1 

    pygame.display.flip()

pygame.quit()
# rotator

# text
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
rotateangle = 0
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(WHITE)
    
    font = pygame.font.SysFont('Times New Roman', 60, False, False)
    
    text = font.render('Pick your agent', True, BLACK)
    text = pygame.transform.rotate(text, rotateangle)
    screen.blit(text, (210, 240)) # images not text

    rotateangle += 1
    pygame.display.flip()

pygame.quit()
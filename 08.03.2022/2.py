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
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(WHITE)
    
    font = pygame.font.SysFont('Times New Roman', 60, False, False)
    font_little = pygame.font.SysFont('Helvetica', 30, False, True)
    
    text = font.render('Pick your agent', True, BLACK)

    title = font_little.render('Competetive', True, BLACK)

    screen.blit(text, (210, 240)) # images not text
    screen.blit(title, (100, 100))

    textr = pygame.transform.rotate(text, 90)
    extr = pygame.transform.rotate(text, 270)
    xtr = pygame.transform.rotate(text, 90)
    
    screen.blit(textr, (50 , 150))
    screen.blit(extr, (130 , 150))

    pygame.display.flip()

pygame.quit()
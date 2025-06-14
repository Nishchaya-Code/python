import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
c=pygame.image.load('images (1).jpeg').convert_alpha()
c=pygame.transform.scale(c,(200,200))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(c,(200,200))
    pygame.display.flip()
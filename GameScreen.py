import pygame
pygame.init()
screen=pygame.display.set_mode((1000,1000))
c=pygame.image.load('images.jpeg').convert_alpha()
c=pygame.transform.scale(c,(1000,1000))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(c,(0,0))
    pygame.display.flip()
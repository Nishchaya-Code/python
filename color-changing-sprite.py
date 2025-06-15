import pygame
import random
pygame.init()
screen=pygame.display.set_mode((750,690))
done=True
def change_color():
    return random.choices(range(256),k=3)
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen,change_color(),pygame.Rect(100,100,200,200))
    pygame.display.flip()
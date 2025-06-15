import pygame
pygame.init()
screen=pygame.display.set_mode((750,690))
done=True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    pygame.draw.circle(screen,(255,0,0),(100,100),50)
    pygame.draw.circle(screen,(0,255,0),(350,345),50,4)
    pygame.display.flip()
import pygame
pygame.init()
screen=pygame.display.set_mode((1000,2500))
pygame.display.set_caption('Custom Events')
p=pygame.rect(500,190,50,50)
o=pygame.rect(50,50,50,50)
red=(200,0,0)
bla=(20,20,20)
whi=(255,255,255)
Pv=True
Ov=True
sprint=True
speed=20
while sprint:
    pygame.time.delay(3)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    key1=pygame.key.get_pressed()
    if key1[pygame.K_LEFT]:
        p.x-=speed
    if key1[pygame.K_RIGHT]:
        p.x+=speed
    if key1[pygame.K_DOWN]:
        p.y+=speed
    if key1[pygame.K_UP]:
        p.y-=speed
    if p.colliderect(o):
        ov=False
    screen.fill(whi)
    if Pv:
        pygame.draw.rect(screen,red,p)
    if Ov:
        pygame.draw.rect(screen,bla,o)
    pygame.display.flip()
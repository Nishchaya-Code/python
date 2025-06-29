import pygame
pygame.init()
screen=pygame.display.set_mode((1000,2500))
pygame.display.set_caption('sprit collision')
p=pygame.Rect(50,50,50,50)
o=pygame.Rect(300,300,50,50)
whi=(255,255,255)
blu=(0,0,255)
red=(255,0,0)
pv=True
ov=True
run=True
speed=5
while run:
    pygame.time.delay(30)
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
    if pv:
        pygame.draw.rect(screen,blu,p)
    if ov:
        pygame.draw.rect(screen,red,o)
    pygame.display.flip()
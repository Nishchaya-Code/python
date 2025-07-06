import pygame
import math
import random
sw=800
sh=400
psx=370
psy=220
esx=2
esy=20
collision=28
bullet_speed=10
got=psy-20
pygame.init()
screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption ("SpaceInvaders")
bg=pygame.image.load("background.png")
p_img=pygame.image.load("player.png")
e_img=pygame.image.load("enemy.png")
b_img=pygame.image.load("bullet.png")
font=pygame.font.Font("freetransbold.tpf",32)
overfont=pygame.font.Font("freetransbold.tpf",64)
enemy=[
    {
      "x":random.randint(0,sw-64),
      "y":random.randint(50,100),
      "dx":esx
    } for i in range(8)
]
bx=0
by=psy
bs="ready"
score=0
px,py=psx,psy
px_c=0


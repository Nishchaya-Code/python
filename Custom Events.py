import pygame


# Initialize Pygame
pygame.init()


# Set up screen
screen = pygame.display.set_mode((1000, 600))  
pygame.display.set_caption('Sprite Collision')


# Define rectangles
p = pygame.Rect(80, 50, 50, 50)   # Player starts near the obstacle
o = pygame.Rect(50, 50, 50, 50)   # Obstacle


# Define colors
red = (200, 0, 0)
bla = (20, 20, 20)
whi = (255, 255, 255)
green = (0, 200, 0)


# Initial states
o_color = bla
pv = True
ov = True
sprint = True
speed = 7


# Game loop
while sprint:
    pygame.time.delay(10)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sprint = False  # Exit game loop


    # Movement
    key1 = pygame.key.get_pressed()
    if key1[pygame.K_LEFT]:
        p.x -= speed
    if key1[pygame.K_RIGHT]:
        p.x += speed
    if key1[pygame.K_DOWN]:
        p.y += speed
    if key1[pygame.K_UP]:
        p.y -= speed


    # Collision detection
    if p.colliderect(o):
        o_color = green
        print("Colliding")
    else:
        o_color = bla


    # Draw everything
    screen.fill(whi)
    if pv:
        pygame.draw.rect(screen, red, p)
    if ov:
        pygame.draw.rect(screen, o_color, o)


    pygame.display.flip()


# Quit
pygame.quit()






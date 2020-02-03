FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')
WHITE = (155, 155, 255)
while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    pygame.display.update()
    fpsClock.tick(FPS)
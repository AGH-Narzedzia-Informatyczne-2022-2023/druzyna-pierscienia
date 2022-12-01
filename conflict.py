import pygame, sys, os

class FRUIT:
    def __init__(self):
        self.x = 5
        self.y = 6



pygame.init()
cell_size = 20




screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,212,75))
    screen.blits(test_surface, (200,250))
    pygame.display.update()
    clock.tick(120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,212,75))
    screen.blits(test_surface, (200,250))
    pygame.display.update()
    clock.tick(120)


print("Hello, here is some text in order to test conflicts...")

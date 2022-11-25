import pygame
from pygame.locals import *
surface = pygame.display.set_mode((400, 380))
def render_background():
        bg = pygame.image.load("x/p.png")
        surface.blit(bg, (0,0))
def draw_block():
    render_background()
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    render_background()


    block = pygame.image.load("x/z.jpg").convert()

    block_x, block_y = 100, 100

    surface.blit(block, (block_x, block_y))

    pygame.display.flip()

    running = True
   


    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
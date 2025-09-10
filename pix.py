import pygame
from random import randint as r

# made by las-r on github
# v1.0

# init
pygame.init()

# initial settings
dw, dh = 800, 800
px = 4

# window
scr = pygame.display.set_mode((dw, dh), pygame.RESIZABLE)
pygame.display.set_caption("visualizer thing idk")

# main loop
run = True
while run:
    # event loop
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
        # mouse buttons
        if e.type == pygame.MOUSEBUTTONDOWN:
            # scroll up
            if e.button == 4:
                scr.fill((0, 0, 0))
                px = max(min(px + 1, dh), 1)
                
            # scroll down
            if e.button == 5:
                scr.fill((0, 0, 0))
                px = max(min(px - 1, dh), 1)
                
            # side buttons
            elif e.button == 7:
                scr.fill((0, 0, 0))
                px = max(min(px + 1, dh), 1)
            elif e.button == 6:
                scr.fill((0, 0, 0))
                px = max(min(px - 1, dh), 1)
                
        # key event
        elif e.type == pygame.KEYDOWN:
            # r key
            if e.key == pygame.K_r:
                scr.fill((0, 0, 0))
            
    # update screen size
    dw, dh = pygame.display.get_window_size()
            
    # draw
    pygame.draw.rect(scr, (r(0, 255), r(0, 255), r(0, 255)), pygame.Rect(r(0, dw // px) * px, r(0, dh // px) * px, px, px))
    pygame.display.flip()
            
# quit
pygame.quit()

# this is so unbelievably useless

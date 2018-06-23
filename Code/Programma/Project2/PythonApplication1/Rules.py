import pygame
from Color import *


def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Rules(screen, BackGround_Rules, button):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround_Rules.image, BackGround_Rules.rect)
        button.Back(screen, 900, 25, 100, 70, "Back")
        pygame.display.update()
    quit()





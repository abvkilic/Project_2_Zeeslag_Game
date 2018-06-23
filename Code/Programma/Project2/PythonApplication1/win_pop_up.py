import pygame
from Color import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def win_screen(screen, BackGround, circle):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(screen, circle)
        pygame.display.update()


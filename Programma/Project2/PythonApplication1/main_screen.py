import pygame
from Color import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main_screen(screen, BackGround, button, circle):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(screen, circle)
        button.Start(screen, 350, 250, 300, 70)
        button.Rules(screen, 25, 25, 100, 70)
        button.Score(screen, 25, 650, 150, 70)
        button.Setting(screen, 350, 350, 300, 70)
        button.Exit(screen, 350, 450, 300, 70)
        pygame.display.update()

    quit()
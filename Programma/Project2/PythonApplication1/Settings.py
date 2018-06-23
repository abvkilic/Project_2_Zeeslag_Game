import pygame
from Color import *
music = True
def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def Settings(screen, button, BackGround_Settings):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(black)
        screen.blit(BackGround_Settings.image, BackGround_Settings.rect)
        button.Back(screen, 900, 25, 100, 70, "Back")
        button.On(screen, 550, 280, 100, 70)
        button.Off(screen, 670, 280, 100, 70)
        pygame.display.update()
    quit()
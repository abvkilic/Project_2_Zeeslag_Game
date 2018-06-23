import pygame
from Color import *
from database import *

def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def Score(screen, button, BackGround_Score):
    while process_events():
        pygame.display.set_caption('Battleport')
        screen.fill(white)
        screen.blit(BackGround_Score.image, BackGround_Score.rect)
        count = 0
        smallText = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects("Name", smallText)
        textRect.center = (400, 250)
        screen.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects("Turns", smallText)
        textRect.center = (550, 250)
        screen.blit(textSurf, textRect)
        for row in download_scores():
            count += 1

            smallText = pygame.font.Font("freesansbold.ttf", 40)
            textSurf, textRect = text_objects(row[1], smallText)
            textRect.center = (400, (250 + (count * 50)))
            screen.blit(textSurf, textRect)

            smallText = pygame.font.Font("freesansbold.ttf", 40)
            textSurf, textRect = text_objects(str(row[2]), smallText)
            textRect.center = (550, (250 + (count * 50)))
            screen.blit(textSurf, textRect)

        button.Back(screen, 900, 25, 100, 70, "Back")
        pygame.display.update()
    quit()

import pygame
from main_game import *
from Color import *
from main_screen import *
from Rules import *
from Settings import *
from Score import *
from Quit import *
from database import *
pygame.init()

#game buttons
class Button:
    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def On(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_green, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, green, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            pygame.mixer.music.unpause()


        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("ON", smallText)
        textRect.center = ((575 + (50 / 2)), (290 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Off(self, screen, x, y, b, h):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_red, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, red, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            pygame.mixer.music.pause()

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("OFF", smallText)
        textRect.center = ((690 + (50 / 2)), (290 + (50 / 2)))
        screen.blit(textSurf, textRect)


    def Start(self, screen, x, y, b, h):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            main_game(screen, button, BackGround_Game)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Start", smallText)
        textRect.center = ((475 + (50 / 2)), (260 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Rules(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 18)
        textSurf, textRect = self.text_objects("Rules", smallText)
        textRect.center = ((47 + (50 / 2)), (35 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Rules(screen, BackGround_Rules, button)

    def Setting(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Settings", smallText)
        textRect.center = ((475 + (50 / 2)), (360 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Settings(screen, button, BackGround_Settings)

    def Exit(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Exit", smallText)
        textRect.center = ((475 + (50 / 2)), (460 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Quit()

    def Score(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Highscore", smallText)
        textRect.center = ((70 + (50 / 2)), (660 + (50 / 2)))
        screen.blit(textSurf, textRect)

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            Score(screen, button, BackGround_Score)

    def Back(self, screen, x, y, b, h, tekst):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_grey, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, grey, (x, y, b, h))
        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1:
            main_screen(screen, BackGround, button, circle)

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = ((920 + (50 / 2)), (35 + (50 / 2)))
        screen.blit(textSurf, textRect)

#game width
width = 1024
height = 768
size = (width, height)

screen = pygame.display.set_mode(size)
button = Button()
pygame.mixer.music.load("gif/mp3/Dank.mp3")
pygame.mixer.music.play(-1,0.0)

circle = pygame.draw.circle(screen, (50,30,90),(90,30),16,5)



def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('gif/water.jpg', [0, 0])
BackGround_Rules = Background('gif/ruls.jpg', [105, 0])
BackGround_Game = Background('gif/Template.jpg', [0,0])
BackGround_Settings = Background('gif/setting.jpg', [0, 0])
BackGround_Score = Background('gif/score.jpg', [0, 0])


#screens
main_screen(screen, BackGround, button, circle)
main_game(screen, button, BackGround_Game)
Settings(screen, button, BackGround_Settings)
Rules(screen, BackGround_Rules)
Score(screen, button, BackGround_Score)
Quit()

import pygame
from Color import *
from database import *

Turn = "P1"
clicked = True
game = True
ChooseBoat = False
text = "Start the game, Select a boat"
CardUsed = False
CardActivatedDef = False
CardActivatedOff = False

global turncount1
turncount1 = 0
turncount2 = 0
class GameButtons:
    def __init__(self):
        self.showCard = True

    def text_objects(self, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    def Fire(self, screen, x, y, b, h, Rangelist):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_red, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, red, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for a in listp1:
                    if a.Selected == True:
                        if a.Fired == False:
                            text = "You missed"
                            for r in Rangelist:
                                for i in listp2:
                                    hit = False
                                    for Position in range(0, len(i.PositionList)):
                                        if r[0] == i.PositionList[Position].x and r[1] == i.PositionList[Position].y:
                                            hit = True
                                if hit == True:
                                    i.Hit()
                                    if i.HP == 0:
                                        text = "You have destroyed " + i.Name
                                    else:
                                        text = "You hit " + i.Name

                            a.Fire()
            elif Turn == "P2":
                for a in listp2:
                    if a.Selected == True:
                        if a.Fired == False:
                            text = "You missed"
                            for r in Rangelist:
                                for i in listp1:
                                    hit = False
                                    for Position in range(0, len(i.PositionList)):
                                        if r[0] == i.PositionList[Position].x and r[1] == i.PositionList[Position].y:
                                            hit = True
                                    if hit == True:
                                        i.Hit()
                                        if i.HP == 0:
                                            text = "You have destroyed " + i.Name
                                        else:
                                            text = "You hit " + i.Name
                            a.Fire()
            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("FIRE!", smallText)
        textRect.center = (((x + 10) + (50 / 2)), ((y + 10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Up(self, screen, x, y, b, h, tekst):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for i in listp1:
                    if i.Selected == True:
                        if i.Move != 0:
                            if tekst == "Up":
                                text = i.Name + " moved up"
                            else:
                                text = i.Name + " moved left"

                        i.MoveUp()
            elif Turn == "P2":
                for i in listp2:
                    if i.Selected == True:
                        if tekst == "Up":
                            text = i.Name + " moved up"
                        else:
                            text = i.Name + " moved left"
                        i.MoveUp()
            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x + 10) + (50 / 2)), ((y + 10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def Down(self, screen, x, y, b, h, tekst):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for i in listp1:
                    if i.Selected == True:
                        if tekst == "Down":
                            text = i.Name + " moved down"
                        else:
                            text = i.Name + " moved right"
                        i.MoveDown()
            elif Turn == "P2":
                for i in listp2:
                    if i.Selected == True:
                        i.MoveDown()
            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x + 10) + (50 / 2)), ((y + 10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def listBoatsDef(self, screen, x, y, b, h, tekst, boat):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global CardActivatedDef
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            boat.AddHP()
            text = "Added 1 health to " + boat.Name
            clicked = False
            CardActivatedDef = False
            print("Click")

        if click[0] != 1 and clicked == False:
            print("Release")
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 12)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x + 50) +(50 / 2)), (y + (50 / 2)))
        screen.blit(textSurf, textRect)
    def listBoatsOff(self, screen, x, y, b, h, tekst, boat):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global CardActivatedOff
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            boat.HitHP()
            clicked = False
            CardActivatedOff = False
            if boat.HP == 0:
                text = "Destroyed " + boat.Name
            else:
                text = "Damaged " + boat.Name
            print("Click")

        if click[0] != 1 and clicked == False:
            print("Release")
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 12)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x + 50) +(50 / 2)), (y + (50 / 2)))
        screen.blit(textSurf, textRect)

    def listBoats(self, screen, x, y, b, h, tekst, boat):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global ChooseBoat
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            boat.Select()
            boat.changeColor()
            text = "Selected " + boat.Name
            clicked = False
            ChooseBoat = True

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 12)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x + 50) +(50 / 2)), (y + (50 / 2)))
        screen.blit(textSurf, textRect)

    def TurnAttack(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for i in listp1:
                    if i.Selected == True:
                        if i.Move != 0:
                            text = i.Name + " turned to attack"
                        else:
                            text = "This boat has no turns left"
                        i.TurnAttack()
            elif Turn == "P2":
                for i in listp2:
                    if i.Selected == True:
                        if i.Move != 0:
                            text = i.Name + " turned to attack"
                        else:
                            text = "This boat has no turns left"
                        i.TurnAttack()
            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Attack", smallText)
        textRect.center = (((x+20) + (50 / 2)), ((y+10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def TurnDefence(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for i in listp1:
                    if i.Selected == True:
                        if i.Move != 0:
                            text = i.Name + " turned to defence"
                        else:
                            text = "This boat has no turns left"
                        i.TurnDefence()

            elif Turn == "P2":
                for i in listp2:
                    if i.Selected == True:
                        if i.Move != 0:
                            text = i.Name + " turned to defence"
                        else:
                            text = "This boat has no turns left"
                        i.TurnDefence()


            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Defence", smallText)
        textRect.center = (((x+20) + (50 / 2)), ((y+10) + (50 / 2)))
        screen.blit(textSurf, textRect)


    def ToSelect(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global clicked
        global ChooseBoat

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_white, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, white, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            if Turn == "P1":
                for i in listp1:
                    i.UnSelect()
            elif Turn == "P2":
                for i in listp2:
                    i.UnSelect()
            ChooseBoat = False
            clicked = False

        if click[0] != 1 and clicked == False:
            clicked = True

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("Back", smallText)
        textRect.center = (((x+15) + (50 / 2)), ((y + 10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def winscreentext(self, screen, test):

        smallText = pygame.font.Font("freesansbold.ttf", 80)
        textSurf, textRect = self.text_objects(test, smallText)
        textRect.center = ((512 + (50 / 2)), (300 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def PlayerTurn(self, screen, x, y, b, h, tekst):
        pygame.draw.rect(screen, white, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x+110) + (50 / 2)), ((y+10) + (50 / 2)))
        screen.blit(textSurf, textRect)

    def textfeed(self, screen, x, y, b, h, a, tekst):
        pygame.draw.rect(screen, white, (x, y, b, h))

        smallText = pygame.font.Font("freesansbold.ttf", 14)
        textSurf, textRect = self.text_objects(tekst, smallText)
        textRect.center = (((x+(a*3)) + (50 / 2)), ((y+10) + (50 / 2)))
        screen.blit(textSurf, textRect)


    def EndTurn(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        global Turn
        global ChooseBoat
        global clicked
        global text
        global CardUsed

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_red, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, red, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and clicked == True:
            # endturn(screen)
            if Turn == "P1":
                player = "Player 1"
            else:
                player = "Player 2"
            text = player + " ended their turn. Select a boat"
            if Turn == "P1":
                global turncount1
                turncount1 += 1
                for i in listp1:
                    i.EndTurn()
                Turn = "P2"
                CardUsed = False
            elif Turn == "P2":
                global turncount2
                turncount2 += 1
                for i in listp2:
                    i.EndTurn()
                Turn = "P1"
                CardUsed = False
            clicked = False
            ChooseBoat = False
        if click[0] != 1 and clicked == False:
            clicked = True


        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects("End turn", smallText)
        textRect.center = ((920 + (50 / 2)), (310 + (50 / 2)))
        screen.blit(textSurf, textRect)

    def DrawCard(self, screen, x, y, b, h):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        imagex = 500
        imagey = 300
        imagew = 125
        imageh = 175

        imagex2 = 300
        imagey2 = 300
        imagew2 = 125
        imageh2 = 175

        imagedef = pygame.image.load("gif/carddef.jpg").convert()
        imageoff = pygame.image.load("gif/cardoff.jpg").convert()

        global Furgo_SaltireP1
        global Santa_BettinaP2
        global Turn
        global CardUsed
        global clicked
        global turncount1
        global turncount2
        global CardActivatedOff
        global CardActivatedDef
        global ChooseBoat
        global text

        if x + b > mouse[0] > x and y + h > mouse[1] > y:  # hor, vert
            pygame.draw.rect(screen, hover_green, (x, y, b, h))  # hor, vert, length, height
        else:
            pygame.draw.rect(screen, green, (x, y, b, h))

        if x + b > mouse[0] > x and y + h > mouse[1] > y and click[0] == 1 and CardUsed == False and self.showCard == True:
            self.showCard = False
            CardUsed = True
            text = "Pick a card"
            print("Click")


        if  self.showCard == False:
            screen.blit(imagedef, pygame.Rect((imagex, imagey),(imagew, imageh)))
            screen.blit(imageoff, pygame.Rect((imagex2, imagey2),(imagew2, imageh2)))
            clicked = True

            if imagex + imagew > mouse[0] > imagex and imagey + imageh > mouse[1] > imagey and click[0] == 1 and clicked == True:
                if Turn == "P1":
                    turncount1 += 1
                    CardActivatedDef = True
                    text = "Select one of boats to add health"
                elif Turn == "P2":
                    turncount2 += 1
                    CardActivatedDef = True
                    text = "Select one of boats to add health"
                self.showCard = True
                clicked == False
            if imagex2 + imagew2 > mouse[0] > imagex2 and imagey2 + imageh2 > mouse[1] > imagey2 and click[0] == 1 and clicked == True:
                if Turn == "P1":
                    turncount1 += 1
                    CardActivatedOff = True
                    text = "Select one of the enemy boats to damage"
                elif Turn == "P2":
                    turncount2 += 1
                    CardActivatedOff = True
                    text = "Select one of the enemy boats to damage"
                self.showCard = True
                clicked == False


        smallText = pygame.font.Font("freesansbold.ttf", 15)
        textSurf, textRect = self.text_objects("Show cards", smallText)
        textRect.center = (((x+20) + (50 / 2)), ((y+10) + (50 / 2)))
        screen.blit(textSurf, textRect)

gamebutton = GameButtons()
def process_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main_game(screen, button, BackGround_Game):
    while process_events():
        pygame.display.set_caption('Battleport')
        pygame.init()
        clock = pygame.time.Clock()
        Done = False
        global MapSize
        MapSize = 21

        TileWidth = 32
        TileHeight = 32
        TileMargin = 1

        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (50, 50, 200)

        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        class MapTile(object):
            def __init__(self, Name, Column, Row):
                self.Name = Name
                self.Column = Column
                self.Row = Row

        class Character(object):
            def __init__(self, Name, color, HP, move, list, HRange, VRange):
                self.Name = Name
                self.Color = color
                self.HP = HP
                self.Move = move
                self.PositionList = list
                self.HRange = HRange
                self.VRange = VRange

                self.ColorReset = self.Color
                self.MoveReset = self.Move
                self.HRangeReset = self.HRange
                self.VRangeReset = self.VRange
                self.Defence = False
                self.Selected = False
                self.Fired = False

            def Fire(self):
                self.Fired = True

            def Select(self):
                self.Selected = True

            def Hit(self):
                self.HP -= 1

            def UnSelect(self):
                self.Selected = False
                self.Color = self.ColorReset

            def changeColor(self):
                self.Color = white

            def TurnDefence(self):
                if self.Move != 0:
                    self.sum = 0
                    self.count = 0

                    for i in self.PositionList:
                        self.sum += i.y
                        i.x += self.count
                        self.count += 1

                    self.avg = self.sum / self.count
                    for new in self.PositionList:
                        new.y = int(self.avg)
                    self.Defence = True
                    self.VRange += 1
                    self.HRange = 0
                    self.Move -= 1

            def TurnAttack(self):
                if self.Move != 0:
                    self.sum = 0
                    self.count = 0

                    for i in self.PositionList:
                        self.sum += i.x
                        self.count += 1
                        i.y += self.count


                    self.avg = self.sum / self.count
                    for new in self.PositionList:
                        new.x = int(self.avg)
                    if Turn == "P1":
                        for i in self.PositionList:
                            i.y -= 2
                    self.Defence = False
                    self.VRange = self.VRangeReset
                    self.HRange = self.HRangeReset
                    self.Move -= 1

            def MoveUp(self):
                self.able = True
                for i in self.PositionList:
                    if i.y == 0:
                        self.able = False
                if self.able == True and self.Move != 0:
                    for i in self.PositionList:
                        if self.Defence == False:
                            i.y -= 1
                        else:
                            i.x -= 1
                    self.Move -= 1

            def MoveDown(self):
                self.able = True
                for i in self.PositionList:
                    if i.y == 20:
                        self.able = False
                if self.able == True and self.Move != 0:
                    for i in self.PositionList:
                        if self.Defence == False:
                            i.y += 1
                        else:
                            i.x += 1
                    self.Move -= 1

            def EndTurn(self):
                self.Move = self.MoveReset
                self.Selected = False
                self.Fired = False
                self.Color = self.ColorReset

            def AddHP(self):
                self.HP += 1
            def HitHP(self):
                self.HP -= 1

        class Map(object):
            global MapSize

            Grid = []

            for Row in range(MapSize):
                Grid.append([])
                for Column in range(MapSize):
                    Grid[Row].append([])

            for Row in range(MapSize):
                for Column in range(MapSize):
                    TempTile = MapTile("WaterTile", Column, Row)
                    Grid[Column][Row].append(TempTile)

            #Player 1 globals

            global MerapiP1
            # global AmadeaP1

            global Silver_whisperP1
            # global Windsurf_Sea_SpiritP1
            # global IntensityP1

            global Furgo_SaltireP1
            # global Santa_BettinaP1

            # PLAYER 1

            # Biggest boats
            MerapiP1 = Character("Merapi", GREEN, 4, 1, [Vector(3, 20), Vector(3, 19), Vector(3, 18), Vector(3, 17)], 4, 4)
            # AmadeaP1 = Character("Amadea ", GREEN, 4, 1, [Vector(5, 20), Vector(5, 19), Vector(5, 18), Vector(5, 17)], 4, 4)

            # Bigger boats
            Silver_whisperP1 = Character("Silver whisper", GREEN, 3, 2, [Vector(9, 20), Vector(9, 19), Vector(9, 18)], 3, 3)
            # Windsurf_Sea_SpiritP1 = Character("Windsurf Sea Spirit", GREEN, 3, 2, [Vector(9, 20), Vector(9, 19), Vector(9, 18)], 3, 3)
            # IntensityP1 = Character("Intensity", GREEN, 3, 2, [Vector(11, 20), Vector(11, 19), Vector(11, 18)], 3, 3)

            # Big boats
            Furgo_SaltireP1 = Character("Furgo Saltire", GREEN, 2, 3, [Vector(13, 10), Vector(13, 9)], 2, 2)
            Santa_BettinaP1 = Character("Santa Bettina", GREEN, 2, 3, [Vector(15, 20), Vector(15, 19)], 2, 2)
            global listp1
            listp1 = [MerapiP1, Silver_whisperP1, Furgo_SaltireP1]

            #Player 2 Globals
            # global MerapiP2
            global AmadeaP2

            # global Silver_whisperP2
            global Windsurf_Sea_SpiritP2
            # global IntensityP2

            # global Furgo_SaltireP2
            global Santa_BettinaP2

            # MerapiP2 = Character("Merapi", RED, 4, 1, [Vector(3, 0), Vector(3, 1), Vector(3, 2), Vector(3, 3)], 4, 4)
            AmadeaP2 = Character("Amadea ", RED, 4, 1, [Vector(3, 0), Vector(3, 1), Vector(3, 2), Vector(3, 3)],4, 4)

            # Bigger boats
            # Silver_whisperP2 = Character("Silver whisper", RED, 3, 2, [Vector(7, 0), Vector(7, 1), Vector(7, 2)], 3, 3)
            Windsurf_Sea_SpiritP2 = Character("Windsurf Sea Spirit", RED, 3, 2, [Vector(9, 0), Vector(9, 1), Vector(9, 2)], 3, 3)
            # IntensityP2 = Character("Intensity", RED, 3, 2, [Vector(11, 0), Vector(11, 1), Vector(11, 2)], 3, 3)

            # Big boats
            # Furgo_SaltireP2 = Character("Furgo Saltire", RED, 2, 3, [Vector(13, 0), Vector(13, 1)], 2, 2)
            Santa_BettinaP2 = Character("Santa Bettina", RED, 2, 3, [Vector(15, 10), Vector(15, 11)], 2, 2)

            global listp2
            listp2 = [AmadeaP2, Windsurf_Sea_SpiritP2, Santa_BettinaP2]

            def update(self):
                for Column in range(MapSize):
                    for Row in range(MapSize):
                        for i in range(len(Map.Grid[Column][Row])):
                            if Map.Grid[Column][Row][i].Column != Column:
                                Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                            elif Map.Grid[Column][Row][i].Name == "Boat":
                                Map.Grid[Column][Row].remove(Map.Grid[Column][Row][i])
                                # Map.Grid[int(Map.Boat.Column)][int(Map.Boat.Row)].append(Map.Boat)

        Map = Map()

        while not Done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Done = True
            screen.fill(BLACK)

            for Row in range(MapSize):
                for Column in range(MapSize):
                    for i in range(0, len(Map.Grid[Column][Row])):
                        Color = BLUE

                    pygame.draw.rect(screen, Color, [(TileMargin + TileWidth) * Column + TileMargin,
                                                     (TileMargin + TileHeight) * Row + TileMargin,
                                                     TileWidth,
                                                     TileHeight])

            for list in listp1:
                if list.HP > 0:
                    for positionnumber in range(0, len(list.PositionList)):
                        x = list.PositionList[positionnumber].x
                        y = list.PositionList[positionnumber].y
                        color = list.Color
                        pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                         (TileMargin + TileHeight) * y + TileMargin,
                                                         TileWidth,
                                                         TileHeight])
                else:
                    for positionnumber in range(0, len(list.PositionList)):
                        x = list.PositionList[positionnumber].x
                        y = list.PositionList[positionnumber].y
                        color = BLACK
                        pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                         (TileMargin + TileHeight) * y + TileMargin,
                                                         TileWidth,
                                                         TileHeight])

            for list in listp2:
                if list.HP > 0:
                    for positionnumber in range(0, len(list.PositionList)):
                        x = list.PositionList[positionnumber].x
                        y = list.PositionList[positionnumber].y
                        color = list.Color
                        pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                         (TileMargin + TileHeight) * y + TileMargin,
                                                         TileWidth,
                                                         TileHeight])
                else:
                    for positionnumber in range(0, len(list.PositionList)):
                        x = list.PositionList[positionnumber].x
                        y = list.PositionList[positionnumber].y
                        color = BLACK
                        pygame.draw.rect(screen, color, [(TileMargin + TileWidth) * x + TileMargin,
                                                         (TileMargin + TileHeight) * y + TileMargin,
                                                         TileWidth,
                                                         TileHeight])
            Rangelist = []
            if Turn == "P1":
                Rangelist = []
                for i in listp1:
                    if i.Selected == True:
                        if i.Defence == False:
                            ymaxTop = 0
                            yminBot = 21
                            for positionnumber in range(0, len(i.PositionList)):
                                if ymaxTop < i.PositionList[positionnumber].y:
                                    ymaxTop = i.PositionList[positionnumber].y

                                if yminBot > i.PositionList[positionnumber].y:
                                    yminBot = i.PositionList[positionnumber].y

                                for a in range(1, (i.HRange + 1)):
                                    y = i.PositionList[positionnumber].y
                                    x = (i.PositionList[positionnumber].x + a)
                                    Rangelist.append([x,y])
                                    if x >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                for a in range(1, (i.HRange + 1)):
                                    y = i.PositionList[positionnumber].y
                                    x = (i.PositionList[positionnumber].x - a)
                                    Rangelist.append([x, y])
                                    if x >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                xas = i.PositionList[positionnumber].x
                            for a in range(1, (i.VRange+1)):
                                y = yminBot - a
                                x = xas
                                Rangelist.append([x, y])
                                if y >= 0:
                                    pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                 (TileMargin + TileHeight) * y + TileMargin,
                                                                 TileWidth,
                                                                 TileHeight])
                            for a in range(1, (i.VRange + 1)):
                                y = ymaxTop + a
                                x = xas
                                Rangelist.append([x, y])
                                if y < 21:
                                    pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                (TileMargin + TileHeight) * y + TileMargin,
                                                                TileWidth,
                                                                TileHeight])

                        elif i.Defence == True:
                            for positionnumber in range(0, len(i.PositionList)):
                                for a in range(1, (i.VRange + 1)):
                                    y = (i.PositionList[positionnumber].y + a)
                                    x = i.PositionList[positionnumber].x
                                    Rangelist.append([x, y])
                                    if y < 21:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                for a in range(1, (i.VRange + 1)):
                                    y = (i.PositionList[positionnumber].y - a)
                                    x = i.PositionList[positionnumber].x
                                    Rangelist.append([x, y])
                                    if y >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
            elif Turn == "P2":
                for i in listp2:
                    if i.Selected == True:
                        if i.Defence == False:
                            ymaxTop = 0
                            yminBot = 21
                            for positionnumber in range(0, len(i.PositionList)):
                                if ymaxTop < i.PositionList[positionnumber].y:
                                    ymaxTop = i.PositionList[positionnumber].y

                                if yminBot > i.PositionList[positionnumber].y:
                                    yminBot = i.PositionList[positionnumber].y

                                for a in range(1, (i.HRange + 1)):
                                    y = i.PositionList[positionnumber].y
                                    x = (i.PositionList[positionnumber].x + a)
                                    Rangelist.append([x, y])
                                    if x >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                for a in range(1, (i.HRange + 1)):
                                    y = i.PositionList[positionnumber].y
                                    x = (i.PositionList[positionnumber].x - a)
                                    Rangelist.append([x, y])
                                    if x >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                xas = i.PositionList[positionnumber].x
                            for a in range(1, (i.VRange+1)):
                                y = yminBot - a
                                x = xas
                                Rangelist.append([x, y])
                                if y >= 0:
                                    pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                 (TileMargin + TileHeight) * y + TileMargin,
                                                                 TileWidth,
                                                                 TileHeight])
                            for a in range(1, (i.VRange + 1)):
                                y = ymaxTop + a
                                x = xas
                                Rangelist.append([x, y])
                                if y < 21:
                                    pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                (TileMargin + TileHeight) * y + TileMargin,
                                                                TileWidth,
                                                                TileHeight])
                        elif i.Defence == True:
                            for positionnumber in range(0, len(i.PositionList)):
                                for a in range(1, (i.VRange + 1)):
                                    y = (i.PositionList[positionnumber].y + a)
                                    x = i.PositionList[positionnumber].x
                                    Rangelist.append([x, y])
                                    if y >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])
                                for a in range(1, (i.VRange + 1)):
                                    y = (i.PositionList[positionnumber].y - a)
                                    x = i.PositionList[positionnumber].x
                                    Rangelist.append([x, y])
                                    if y >= 0:
                                        pygame.draw.rect(screen, grey, [(TileMargin + TileWidth) * x + TileMargin,
                                                                        (TileMargin + TileHeight) * y + TileMargin,
                                                                        TileWidth,
                                                                        TileHeight])

            winp1 = True
            winp2 = True
            for hp in listp1:
                if hp.HP > 0:
                    winp2 = False

            for hp in listp2:
                if hp.HP > 0:
                    winp1 = False

            clock.tick(30)

            button.Back(screen, 900, 25, 100, 70, "Quit")
            gamebutton.EndTurn(screen, 900, 300, 100, 70)

            #Sjors van Gelderen had toestemming gegeven om 3 boten te plaatsen per speler
            if CardActivatedOff == True:
                count = 0
                if Turn == "P1":
                    for i in listp2:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoatsOff(screen, x, y, b, h, name, i)
                elif Turn == "P2":
                    for i in listp1:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoatsOff(screen, x, y, b, h, name, i)
            elif CardActivatedDef == True:
                count = 0
                if Turn == "P1":
                    for i in listp1:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoatsDef(screen, x, y, b, h, name, i)
                elif Turn == "P2":
                    for i in listp2:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoatsDef(screen, x, y, b, h, name, i)
            elif ChooseBoat == False:
                count = 0
                if Turn == "P1":
                    for i in listp1:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoats(screen, x, y, b, h, name, i)
                elif Turn == "P2":
                    for i in listp2:
                        if i.HP > 0:
                            count += 1
                            x = 700
                            y = 400 + (50 * count)
                            b = 150
                            h = 50
                            name = i.Name + " - HP: " + str(i.HP)
                            gamebutton.listBoats(screen, x, y, b, h, name, i)
            else:
                if Turn == "P1":
                    for i in listp1:
                        if i.Selected == True:
                            if i.Defence == False:
                                gamebutton.TurnDefence(screen, 900, 550, 100, 70)
                            else:
                                gamebutton.TurnAttack(screen, 900, 550, 100, 70)
                elif Turn == "P2":
                    for i in listp2:
                        if i.Selected == True:
                            if i.Defence == False:
                                gamebutton.TurnDefence(screen, 900, 550, 100, 70)
                            else:
                                gamebutton.TurnAttack(screen, 900, 550, 100, 70)

                textUp = "Up"
                textDown = "Down"

                if Turn == "P1":
                    for i in listp1:
                        if i.Selected == True:
                            if i.Defence == True:
                                textUp = "Left"
                                textDown = "Right"


                elif Turn == "P2":
                    for i in listp2:
                        if i.Selected == True:
                            if i.Defence == True:
                                textUp = "Left"
                                textDown = "Right"

                gamebutton.ToSelect(screen, 750, 550, 100, 70)
                gamebutton.Up(screen, 750, 450, 100, 70, textUp)
                gamebutton.Down(screen, 900, 450, 100, 70, textDown)
                gamebutton.Fire(screen, 750, 650, 100, 70, Rangelist)

            if Turn == "P1":
                tekst = "Player 1's turn"
            elif Turn == "P2":
                tekst = "Player 2's turn"

            test = 0
            for a in range(1, len(text)+1):
                test = a

            button.Back(screen, 900, 25, 100, 70, "Quit")
            gamebutton.DrawCard(screen, 900, 650, 100, 70)
            gamebutton.EndTurn(screen, 900, 300, 100, 70)
            gamebutton.PlayerTurn(screen, 710, 150, 300, 70, tekst)
            gamebutton.textfeed(screen, 710, 220, 300, 70, test, text)


            if winp1 == True or winp2 == True:
                global game
                if game == True:
                    print("WRM WERKT DIT NIET")
                    if winp1 == True:
                        upload_score("P1", turncount1)
                    elif winp2 == True:
                        upload_score("P2", turncount2)
                    game = False


                screen.fill(GREEN)
                gamebutton.winscreentext(screen,"Victory")
                button.Back(screen, 900, 25, 100, 70, "Back")

            pygame.display.flip()

            Map.update()
        quit()

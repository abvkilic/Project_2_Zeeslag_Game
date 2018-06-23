import pygame
from database import *
from random import randint


class Cards:
    def __init__(self, type, name, amount):
        self.Type = type
        self.Name = name
        self.Amount = amount

    def pick_card(self):
        random = randint(0, 2)
        if(random == 0):
            random = randint(0,4)
            if(random == 0):
                return FMJ_upgrade
            if(random == 1):
                return Rifling
            if(random == 2):
                return Advanced_Rifling
            if(random == 3):
                return Naval_Mine
            if(random == 4):
                return EMP_upgrade
        if(random == 1):
            random = randint(0,3)
            if(random == 0):
                return Reinforced_Hull
            if(random == 1):
                return Sonar
            if(random == 2):
                return Smokescreen
            if(random == 3):
                return Sabotage
        if(random == 2)
            random = randint(0,4)
            if(random == 0)
                return Backup
            if(random == 1)
                return Extra_Fuel
            if(random == 2)
                return Extra_Fuel_II
            if(random == 3)
                return Rally
            if(random == 4)
                return Adrenaline_rush




# Offensieve kaarten
FMJ_upgrade = Cards("Offensieve", "FMJ upgrade", 2)
Rifling = Cards("Offensieve", "Rifling", 2)
Advanced_Rifling = Cards("Offensieve", "Advanced Rifling", 2)
Naval_Mine = Cards("Offensieve", "Naval Mine", 6)
EMP_upgrade = Cards("Offensieve", "EMP upgrade", 4)

# Defensieve kaarten
Reinforced_Hull = Cards("Defensieve", "Reinforced Hull", 2)
Sonar = Cards("Defensieve", "Sonar", 4)
Smokescreen = Cards("Defensieve", "Smokescreen", 2)
Sabotage = Cards("Defensieve", "Sabotage", 2)

# Hulp kaarten
Backup = Cards("Hulp", "Backup", 2)
Extra_Fuel_II = Cards("Hulp", "Extra Fuel II", 4)
Extra_Fuel = Cards("Hulp", "Extra Fuel", 6)
Rally = Cards("Hulp", "Rally", 1)
Adrenaline_rush = Cards("Hulp", "Adrenaline rush", 4)

#Special kaarten
Repair = Cards("Special", "Repair", 2)
Flak_armor = Cards("Special", "Flak armor", 2)
Hack_Intel = Cards("Special", "Hack Intel", 1)
Far_sight = Cards("Special", "Far sight", 1)
Aluminum_hull = Cards("Special", "Aluminum hull", 1)
Jack_Sparrow = Cards("Special", "Jack Sparrow", 1)



class BoatSmall:
    def __init__(self):
        self.Name = "Furgo Saltire"
        self.HP = 2
        self.Move = 3
        self.HorRange = 2
        self.VerRange = 2

    def Defensive(self):
        self.HorRange = 0
        self.VerRange = 3

    def Move(self):
        self.Move -= 1

    def EndTurn(self):
        self.Move = 3

    def GetHit(self):
        self.HP -= 1

class BoatMiddle:
    def __init__(self):
        self.Name = "Silver whisper"
        self.HP = 3
        self.Move = 2
        self.HorRange = 3
        self.VerRange = 3

    def Defensive(self):
        self.HorRange = 0
        self.VerRange = 4

    def Move(self):
        self.Move -= 1

    def EndTurn(self):
        self.Move = 2

    def GetHit(self):
        self.HP -= 1

class BoatBig:
    def __init__(self):
        self.Name = "Merapi"
        self.HP = 4
        self.Move = 1
        self.HorRange = 4
        self.VerRange = 4

    def Defensive(self):
        self.HorRange = 0
        self.VerRange = 5

    def Move(self):
        self.Move -= 1

    def EndTurn(self):
        self.Move = 2

    def GetHit(self):
        self.HP -= 1
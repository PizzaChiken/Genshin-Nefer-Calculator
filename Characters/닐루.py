class NilouP1Buff: 
    def __init__(self, Game, Character, Active):
        self.Name = 'Nilou P1 EM'
        self.Proportional = False
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

        self.Active = Active

    
    def Apply(self, BuffedCharacter, Print):
        Stat = 'EM'
        Amount = 100 if self.Active else 0 
        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

    
class NilouC2Debuff: 
    def __init__(self, Game, Character, Constellation):
        self.Name = 'Nilou C2 Res'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character
        self.Constellation = Constellation
    
    def Apply(self, DebuffedEnemy, Print):
        
        Constellation = self.Character.Constellation if self.Character is not None else self.Constellation
        if Constellation >= 2:
            Stat1 = 'HydroRes'
            Stat2 = 'DendroRes'
            Amount = -0.35
            DebuffedEnemy.DebuffedStat[Stat1] += Amount
            DebuffedEnemy.DebuffedStat[Stat2] += Amount
            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat1:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat1]:<5.3f}")
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat2:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat2]:<5.3f}")

def AddNilouTemp(Game, Constellation, P1EMActive):
    Game.AddEffect(NilouP1Buff(Game, Character=None, Active=P1EMActive))
    Game.AddEffect(NilouC2Debuff(Game, Character=None, Constellation=Constellation))


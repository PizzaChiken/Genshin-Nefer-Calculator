from Game import Game
class SilkenMoonsSerenade:
    def __init__(self, Game, Character, PC, Moonsign = 2):
        assert PC in [2, 4]

        self.StatList = {
            'ER' : 0.2 
        }

        if PC == 4:
            self.EffectList = [SilkenMoonsSerenadeBuff(Game, Character, PC, Moonsign), 
                               SilkenMoonsSerenadeAttackEffect(Game, Character, PC, Moonsign)]

class SilkenMoonsSerenadeBuff: 
    def __init__(self, Game, Character, PC, Moonsign):
        self.Name = 'SilkenMoonsSerenade EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.PC = PC

        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, BuffedCharacter, Print):
        if self.PC == 4:
            Stat = 'EM'
            Amount = self.Moonsign * 60
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class SilkenMoonsSerenadeAttackEffect: 
    def __init__(self, Game, Character, PC, Moonsign):
        self.Name = 'SilkenMoonsSerenade ReactionBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
        self.PC = PC

        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.PC == 4:
            if 'Lunar' in AttackType:
                AttackingCharacterStat['ReactionBonus']  += 0.1
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddSilkenMoonsSerenadeTemp(Game, PC, Moonsign):
    Game.AddEffect(SilkenMoonsSerenadeBuff(Game, Character=None, PC=PC, Moonsign=Moonsign))
    Game.AddEffect(SilkenMoonsSerenadeAttackEffect(Game, Character=None, PC=PC, Moonsign=Moonsign))

from Game import Game
class SilkenMoonsSerenade:
    def __init__(self, Character, PC, Moonsign = 2):
        assert PC in [2, 4]

        self.StatList = {
            'ER' : 0.2 
        }

        if PC == 4:
            self.EffectList = [SilkenMoonsSerenadeBuff(Character, PC, Moonsign), 
                               SilkenMoonsSerenadeAttackEffect(Character, PC, Moonsign)]

class SilkenMoonsSerenadeBuff: 
    def __init__(self, Character=None, PC=4, Moonsign=2):
        self.Name = 'SilkenMoonsSerenade EM'
        self.Proportional = False
        self.Type = 'Buff'

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
    def __init__(self, Character=None, PC=4, Moonsign=2):
        self.Name = 'SilkenMoonsSerenade ReactionBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.PC = PC
        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.PC == 4:
            if 'Lunar' in AttackType:
                AttackingCharacterStat['ReactionBonus']  += 0.1
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddSilkenMoonsSerenadeTemp(Game:Game, PC, Moonsign):
    Game.AddEffect(SilkenMoonsSerenadeBuff(PC=PC, Moonsign=Moonsign))
    Game.AddEffect(SilkenMoonsSerenadeAttackEffect(PC=PC, Moonsign=Moonsign))

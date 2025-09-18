# 달을 엮는 밤노래
from Game import Game

#체크리스트
# 파티원마 (Buff)  (complete) 
# 파티달반응피증(AttackEffect)  (complete) 

class SilkenMoonsSerenade:
    def __init__(self, Game, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'ER' : 0.2 
        }

        if PC == 4:
            self.EffectList = [SilkenMoonsSerenadeBuff(Game, Character, PC), 
                               SilkenMoonsSerenadeAttackEffect(Game, Character, PC)]
        else:
            self.EffectList = []

class SilkenMoonsSerenadeBuff: 
    def __init__(self, Game, Character, PC):
        self.Name = 'SilkenMoonsSerenade EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.PC = PC


    def Apply(self, BuffedCharacter, Print):
        if self.PC == 4:
            Stat = 'EM'
            Amount = min(2, self.Game.Moonsign) * 60
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class SilkenMoonsSerenadeAttackEffect: 
    def __init__(self, Game, Character, PC):
        self.Name = 'SilkenMoonsSerenade ReactionBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
        self.PC = PC


    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if self.PC == 4:
            if AttackType in ['DirectLunarCharged', 'LunarCharged', 'DirectLunarBloom']:
                AttackingCharacterStat['ReactionBonus']  += 0.1
        
        return AttackingCharacterStat, TargetedEnemyStat


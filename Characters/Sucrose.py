
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# P1 EM 파티 (Buff)  (Complete)
# p2 EM 파티 (Buff)  (Complete)
# C2 궁횟수          (Complete)
# C6 피증 (Buff)     (Complete)

class SucroseClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, UltElement = 'Electro', P1Element = ['Electro']):
        super().__init__(Game=Game,
                         Name='Sucrose',
                         Weapon='Catalyst',
                         Element='Anemo',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
        
        if Level == 90:
            self.BaseStat['BaseHP'] += 9244
            self.BaseStat['BaseATK'] += 170
            self.BaseStat['BaseDEF'] += 703
        elif Level == 100:
            self.BaseStat['BaseHP'] += 9883
            self.BaseStat['BaseATK'] += 213
            self.BaseStat['BaseDEF'] += 752
        else:
            raise ValueError
        self.BaseStat['AnemoDMGBonus'] += 0.24

        self.UltElement = UltElement
        self.P1Element = P1Element

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3
        
        self.Game.AddEffect(SurcroseP1Buff(Game, self))
        self.Game.AddEffect(SurcroseP2Buff(Game, self))
        self.Game.AddEffect(SurcroseC6Buff(Game, self))
    
        
    def Skill(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 3.80, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 4.49, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬',
                            AttackType = 'Basic',
                            AttackElement = 'Anemo',
                            DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.66, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 3.15, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발',
                            AttackType = 'Basic',
                            AttackElement = 'Anemo',
                            DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltElemental(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.792, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.935, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 부가원소',
                            AttackType = 'Basic',
                            AttackElement = self.UltElement,
                            DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
   

    def UltCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        Count = 4 if self.Constellation >= 2 else 3
        for i in range(Count):
            DMG += self.Ult(TargetedEnemy, None, False)
            DMG += self.UltElemental(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG
    
    def Rotation(self, TargetedEnemy):
        DMG = 0
        DMG += self.Skill(TargetedEnemy, None, True)
        DMG += self.UltCombine(TargetedEnemy, True)
        return DMG

class SurcroseP1Buff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Surcrose P1 EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter.Element in self.Character.P1Element:
            Stat = 'EM'
            Amount = 50
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class SurcroseP2Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Surcrose P2 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter is not self.Character:
            Stat = 'EM'
            Amount = self.Character.BuffedStat['EM'] * 0.2
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class SurcroseC6Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Surcrose C6 ElementalDMG'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if self.Character.Constellation >= 6:
            Stat = f'{self.Character.UltElement}DMGBonus'
            Amount = 0.2
            BuffedCharacter.BaseStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BaseStat[Stat]:<5.3f}")



    


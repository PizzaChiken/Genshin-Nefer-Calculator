
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# Q버프 (온필드에만) (Buff) (Complete)
# 1돌 버프 추가 (Buff)       (Complete)
# 6돌 동작 (AttackEffect)    (Complete)

# 체크리스트
class BennettClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0):
        super().__init__(Game=Game,
                         Name='Bennett',
                         Weapon='Sword',
                         Element='Pyro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
        
        if Level == 90:
            self.BaseStat['BaseHP'] += 12397
            self.BaseStat['BaseATK'] += 191
            self.BaseStat['BaseDEF'] += 771
        elif Level == 100:
            self.BaseStat['BaseHP'] += 13255
            self.BaseStat['BaseATK'] += 240
            self.BaseStat['BaseDEF'] += 825
        else:
            raise ValueError
        self.BaseStat['ER'] += 0.267
        
        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3

        self.Game.AddEffect(BennettQBuff(Game, self))
        self.Game.AddEffect(BennettC6Buff(Game, self))
    
        
    def SkillPress(self, TargetedEnemy, Reaction=None, Print=True):
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.480, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.920, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 터치',
                           AttackType = 'Basic',
                           AttackElement = 'Pyro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 4.190, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 4.950, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발',
                           AttackType = 'Basic',
                           AttackElement = 'Pyro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    
    def Rotation(self, TargetedEnemy):
        DMG = 0
        DMG += self.Ult(TargetedEnemy, None, True)
        DMG += self.Overloaded(TargetedEnemy, True)
        DMG += self.SkillPress(TargetedEnemy, '증발', True)
        return DMG

class BennettQBuff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Bennett Q ATK'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Game.OnField:
            if self.Character.SkillLevel['Ult'] == 10:
                Multiplier = 1.01
            elif self.Character.SkillLevel['Ult'] == 13:
                Multiplier = 1.19
            else:
                raise NotImplementedError

            if self.Character.Constellation >= 1:
                Multiplier += 0.2
            
            Stat = 'AdditiveATK'
            Amount = self.Character.BuffedStat['BaseATK'] * Multiplier
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class BennettC6Buff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Bennett C6 PyroDMGBonus'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Game.OnField:
            if self.Character.Constellation >= 6:
                if BuffedCharacter.Weapon in ['Sword', 'Claymore', 'Polearm']:
                    Stat = 'PyroDMGBonus'
                    Amount = 0.15
                    BuffedCharacter.BuffedStat[Stat] += Amount
                    if Print:
                        print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


        
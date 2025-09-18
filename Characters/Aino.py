
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# P1 궁횟수                                       (complete)
# P2 궁 강화(자신만 적용 확인) (AttackEffect)      (complete)
# C1 EM(파티) (Buff)                              (complete)
# C2 추가피해                                     (complete)
# C6 파티 반응피해(AttackEffect)                  (Complete)

class AinoClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, C1Active=True):
        super().__init__(Game=Game,
                         Name='Aino',
                         Weapon='Claymore',
                         Element='Hydro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)

        if Level == 90:
            self.BaseStat['BaseHP'] += 11201
            self.BaseStat['BaseATK'] += 242
            self.BaseStat['BaseDEF'] += 607
        elif Level == 100:
            self.BaseStat['BaseHP'] += 11976
            self.BaseStat['BaseATK'] += 304
            self.BaseStat['BaseDEF'] += 649
        else:
            raise ValueError
        self.BaseStat['EM'] += 96
  
        self.Game.Moonsign += 1
        self.C1Active = C1Active

        if self.Constellation >= 3:
            self.SkillLevel['Ult'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Skill'] += 3

        self.Game.AddEffect(AinoP2AttackEffect(Game, self))
        self.Game.AddEffect(AinoC1Buff(Game, self))
        self.Game.AddEffect(AinoC6AttackEffect(Game, self))
    
        
    def Skill(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.118+3.398, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.394+4.012, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬',
                           AttackType = 'Basic',
                           AttackElement = 'Hydro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.362, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.427, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName=f'{self.Name} 원소폭발',
                           AttackType='Basic',
                           AttackElement='Hydro',
                           DMGType='Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def C2Damage(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 0.25, 'DEF' : 0., 'EM' : 1.0}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 2돌 피해',
                           AttackType = 'Basic',
                           AttackElement = 'Hydro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    
    def UltCombine(self, TargetedEnemy, Print=True):
        DMG = 0

        if self.Game.Moonsign >= 2:
            for i in range(20):
                DMG += self.Ult(TargetedEnemy, None, False)
        else:
            for i in range(10):
                DMG += self.Ult(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG

    
    def Rotation(self, TargetedEnemy):
        DMG = 0
        DMG += self.Skill(TargetedEnemy, None, True)
        DMG += self.UltCombine(TargetedEnemy, True)

        if self.Constellation >= 2:
            if self.Game.OnField != self:
                DMG += self.C2Damage(TargetedEnemy, None, True)
                DMG += self.C2Damage(TargetedEnemy, None, True)
                DMG += self.C2Damage(TargetedEnemy, None, True)
        
        return DMG

class AinoP2AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Aino P2 Ult DMGBonus'
        self.Type = 'AttackEffect'

        self.Game=Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if DMGType == 'Ult':
                EM = self.Character.FinalStat['EM']
                Multiplier = 0.5
                AttackingCharacterStat['AdditiveBaseDMGBonus'] += EM * Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat

class AinoC1Buff:
    def __init__(self, Game, Character):
        self.Name = 'Aino C1 EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if self.Character.Constellation >= 1:
            if self.Character.C1Active:
                if BuffedCharacter in (self.Character, self.Game.OnField):
                    Stat = 'EM'
                    Amount = 80
                    BuffedCharacter.BuffedStat[Stat] += Amount
                    if Print:
                        print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class AinoC6AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Aino C6 ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType in ['DirectLunarCharged', 'LunarCharged', 'ElectroCharged']:
            if self.Character.Constellation >= 6:
                Amount = 0.35 if self.Game.Moonsign >= 2 else 0.15
                AttackingCharacterStat['ReactionBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat
    
    


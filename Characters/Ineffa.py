
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# P1 추가 달감전 피해 적용확인                              (complete)
# P2 원마 버프(온필드만 되는지, 궁발동시에만 되는지) (Buff)  (complete)
# P3 파티 달감전 피증 (파티원 적용 검증) (AttackEffect)     (complete)
# C1 파티 달감전 피증 (파티원 적용 검증) (AttackEffect)      (complete)
# C2 궁 추가 피해 적용 확인                                 (complete)
# C6 추가피해 동작 확인                                     (complete)

class IneffaClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, thunderclouds=True, UltActive=True):
        super().__init__(Game=Game,
                         Name='Ineffa',
                         Weapon='Polearm',
                         Element='Electro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
        if Level == 90:
            self.BaseStat['BaseHP'] += 12613
            self.BaseStat['BaseATK'] += 330
            self.BaseStat['BaseDEF'] += 828
        elif Level == 100:
            self.BaseStat['BaseHP'] += 13510
            self.BaseStat['BaseATK'] += 404
            self.BaseStat['BaseDEF'] += 887
        else:
            raise ValueError
        self.BaseStat['CR'] += 0.192
        
        self.Game.Moonsign += 1
        self.thunderclouds = thunderclouds
        self.UltActive = UltActive

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3
        
        self.Game.AddEffect(IneffaP2Buff(Game, self))
        self.Game.AddEffect(IneffaP3AttackEffect(Game, self))
        self.Game.AddEffect(IneffaC1AttackEffect(Game, self))
    
        
    def SkillActive(self, TargetedEnemy, Reaction=None, Print=True):
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.555, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.836, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 발동',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def BirgittaDischarge(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.728, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.040, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 비르지타 방전',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def BirgittaDischargeP1(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 0.65, 'DEF' : 0., 'EM' : 0.}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 비르지타 추가 공격',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult(self, TargetedEnemy, Reaction=None, Print=True):
        
        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 12.182, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 14.382, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltC2(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 3.0, 'DEF' : 0., 'EM' : 0.}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 2돌 추가피해',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def C6Damage(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 1.35, 'DEF' : 0., 'EM' : 0.}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 6돌 피해',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def BirgittaDischargeCombine(self, TargetedEnemy, Print=True):
        DMG = 0

        DMG += self.BirgittaDischarge(TargetedEnemy, None, False)
        if self.thunderclouds:
            DMG += self.BirgittaDischargeP1(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 비르지타 방전 총합 피해 : {DMG}')
        return DMG

    def UltCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.Ult(TargetedEnemy, None, False)
        if self.Constellation >= 2:
            DMG += self.UltC2(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG
    
    def Rotation(self, TargetedEnemy, BirgitaCount, C6Count):
        DMG = 0
        DMG += self.SkillActive(TargetedEnemy, None, True)
        DMG += self.UltCombine(TargetedEnemy, True)
        
        for i in range(BirgitaCount):
            DMG += self.BirgittaDischargeCombine(TargetedEnemy, True)

        for i in range(C6Count):
            if self.Constellation >= 6:
                DMG += self.C6Damage(TargetedEnemy, None, True)

        return DMG

class IneffaP2Buff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Ineffa P2 Ult EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter in (self.Character, self.Game.OnField):
            if self.Character.UltActive:
                ATK = self.Character.BuffedStat['BaseATK'] * (1 + self.Character.BuffedStat['%ATK']) + self.Character.BuffedStat['AdditiveATK']
                Stat = 'EM'
                Amount = ATK * 0.06
                BuffedCharacter.FinalStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class IneffaP3AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Ineffa P3 LunarChargeBaseDMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType in ['DirectLunarCharged', 'LunarCharged']:
            ATK = self.Character.FinalStat['BaseATK'] * (1 + self.Character.FinalStat['%ATK']) + self.Character.FinalStat['AdditiveATK']
            Amount =  min(0.14, ATK/100 * 0.007)

            AttackingCharacterStat['LunarChargedBaseDMGBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class IneffaC1AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Ineffa C1 ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType in ['DirectLunarCharged', 'LunarCharged']:
            if self.Character.Constellation >= 1:
                ATK = self.Character.FinalStat['BaseATK'] * (1 + self.Character.FinalStat['%ATK']) + self.Character.FinalStat['AdditiveATK']
                Amount =  min(0.5, ATK/100 * 0.025)

                AttackingCharacterStat['ReactionBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat
    


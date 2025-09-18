
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# 일반궁 특수궁 적용                            (complete)
# P1 플린스 달피증(자신만 적용) (AttackEffect)   (complete)
# P2 플린스 원마(자신만적용) (Buff)               (complete)
# P3 파티 달피증 (파티전체적용) (AttackEffect)    (complete)
# C1 사이클                                       (complete)
# C2 추가뎀적용, 내성깍(Debuff)                  (complete)
# C4 원마버프(자신만) (Buff)                     (complete)
# C6 승격 (자신, 파티) (AttackEffect)            (complete)
 
class FlinsClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, thunderclouds=True):
        super().__init__(Game=Game,
                         Name='Flins',
                         Weapon='Polearm',
                         Element='Electro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
        
        if Level == 90:
            self.BaseStat['BaseHP'] += 12491
            self.BaseStat['BaseATK'] += 352
            self.BaseStat['BaseDEF'] += 809
        elif Level == 100:
            self.BaseStat['BaseHP'] += 13379
            self.BaseStat['BaseATK'] += 431
            self.BaseStat['BaseDEF'] += 866
        else:
            raise ValueError
        self.BaseStat['CD'] += 0.384
        
        self.Game.Moonsign += 1
        self.thunderclouds = thunderclouds

        if self.Constellation >= 3:
            self.SkillLevel['Ult'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Skill'] += 3

        self.Game.AddEffect(FlinsP1AttackEffect(Game, self))
        self.Game.AddEffect(FlinsP2Buff(Game, self))
        self.Game.AddEffect(FlinsP3AttackEffect(Game, self))
        self.Game.AddEffect(FlinsC2Debuff(Game, self))
        self.Game.AddEffect(FlinsC4Buff(Game, self))
        self.Game.AddEffect(FlinsC6AttackEffect(Game, self))
    
        
    def SkillNA1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.048, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.238, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 푸른불 일반공격 1단',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillNA2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.058, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.249, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 푸른불 일반공격 2단',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillNA3(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.311, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.548, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 푸른불 일반공격 3단',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillNA4(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.751*2, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.887*2, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 푸른불 일반공격 4단',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillNA5(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.800, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.125, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 푸른불 일반공격 5단',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)

    def NorthlandSpearstorm(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 3.211, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 3.791, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 북국의 장창',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltNoramlInit(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 4.677, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 5.522, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반 원소폭발 발동',
                           AttackType = 'Basic',
                           AttackElement = 'Electro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltNoramlMiddel(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.292, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.345, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반 원소폭발 1단',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltNoramlFinal(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.105, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.485, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반 원소폭발 2단',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltSpecial1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.286, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.518, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 특수 원소폭발 1단',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def UltSpecial2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.871, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.209, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 특수 원소폭발 2단',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def C2Damage(self, TargetedEnemy, Reaction=None, Print=True):
        
        Multiplier = {'HP' : 0., 'ATK' : 0.5, 'DEF' : 0., 'EM' : 0.}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 2돌 피해',
                           AttackType = 'DirectLunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)

    def NormalUltCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.UltNoramlInit(TargetedEnemy, None, False)
        DMG += self.UltNoramlMiddel(TargetedEnemy, None, False)
        DMG += self.UltNoramlMiddel(TargetedEnemy, None, False)
        DMG += self.UltNoramlFinal(TargetedEnemy, None, False)

        if self.thunderclouds==True and self.Game.Moonsign >= 2:
            DMG += self.UltNoramlMiddel(TargetedEnemy, None, False)
            DMG += self.UltNoramlMiddel(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 일반 원소폭발 총합 피해 : {DMG}')
        return DMG

    def SpecialUltCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.UltSpecial1(TargetedEnemy, None, False)

        if self.thunderclouds==True and self.Game.Moonsign >= 2:
            DMG += self.UltSpecial2(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 특수 원소폭발 총합 피해 : {DMG}')
        return DMG
    
    def RotationC0(self, TargetedEnemy):
        assert self.Constellation == 0
        # E N1 EQ 2N5d EQ N1
        DMG = 0
        DMG += self.SkillNA1(TargetedEnemy, None, True)

        DMG += self.NorthlandSpearstorm(TargetedEnemy, None, True)
        DMG += self.SpecialUltCombine(TargetedEnemy, True)
        
        DMG += self.SkillNA1(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)
        DMG += self.SkillNA4(TargetedEnemy, None, True)
        DMG += self.SkillNA5(TargetedEnemy, None, True)
        DMG += self.SkillNA1(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)
        DMG += self.SkillNA4(TargetedEnemy, None, True)
        DMG += self.SkillNA5(TargetedEnemy, None, True)

        DMG += self.NorthlandSpearstorm(TargetedEnemy, None, True)
        DMG += self.SpecialUltCombine(TargetedEnemy, True)

        DMG += self.SkillNA1(TargetedEnemy, None, True)

        return DMG

    def RotationC1(self, TargetedEnemy):
        assert self.Constellation >= 1
        # E EQ 2N3d EQ 2N3d EQ N1
        DMG = 0
        DMG += self.NorthlandSpearstorm(TargetedEnemy, None, True)
        DMG += self.SpecialUltCombine(TargetedEnemy, True)
        
        DMG += self.SkillNA1(TargetedEnemy, None, True)
        if self.Constellation>=2:
            DMG += self.C2Damage(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)
        DMG += self.SkillNA1(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)

        DMG += self.NorthlandSpearstorm(TargetedEnemy, None, True)
        DMG += self.SpecialUltCombine(TargetedEnemy, True)

        DMG += self.SkillNA1(TargetedEnemy, None, True)
        if self.Constellation>=2:
            DMG += self.C2Damage(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)
        DMG += self.SkillNA1(TargetedEnemy, None, True)
        DMG += self.SkillNA2(TargetedEnemy, None, True)
        DMG += self.SkillNA3(TargetedEnemy, None, True)

        DMG += self.NorthlandSpearstorm(TargetedEnemy, None, True)
        DMG += self.SpecialUltCombine(TargetedEnemy, True)

        DMG += self.SkillNA1(TargetedEnemy, None, True)
        if self.Constellation>=2:
            DMG += self.C2Damage(TargetedEnemy, None, True)
        
        return DMG

    def Rotation(self, TargetedEnemy):
        if self.Constellation == 0:
            return self.RotationC0(TargetedEnemy)
        elif self.Constellation >= 1:
            return self.RotationC1(TargetedEnemy)
        else:
            raise ValueError

class FlinsP1AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Flins P1 ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if AttackType in ['DirectLunarCharged', 'LunarCharged']:
                if self.Game.Moonsign >= 2:
                    AttackingCharacterStat['ReactionBonus'] += 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat

class FlinsP2Buff:
    def __init__(self, Game, Character):
        self.Name = 'Flins P2 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            ATK = self.Character.BuffedStat['BaseATK'] * (1 + self.Character.BuffedStat['%ATK']) + self.Character.BuffedStat['AdditiveATK']
            Stat = 'EM'
            Amount = min(160, ATK * 0.08)
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class FlinsP3AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Flins P3 LunarChargeBaseDMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType in ['DirectLunarCharged', 'LunarCharged']:
            ATK = self.Character.FinalStat['BaseATK'] * (1 + self.Character.FinalStat['%ATK']) + self.Character.FinalStat['AdditiveATK']
            Amount =  min(0.14, ATK/100 * 0.007)

            AttackingCharacterStat['LunarChargedBaseDMGBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class FlinsC2Debuff: 
    def __init__(self, Game, Character):
        self.Name = 'Flins C2 Res'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, DebuffedEnemy, Print):
        if self.Character.Constellation>=2:
            Stat = 'ElectroRes'
            Amount = -0.25

            DebuffedEnemy.DebuffedStat[Stat] += Amount
            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")
            
class FlinsC4Buff:
    def __init__(self, Game, Character):
        self.Name = 'Flins C4 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.Character.Constellation>=4:
                ATK = self.Character.BuffedStat['BaseATK'] * (1 + self.Character.BuffedStat['%ATK']) + self.Character.BuffedStat['AdditiveATK']
                Stat = 'EM'
                Amount = min(220, ATK * 0.1)
                BuffedCharacter.FinalStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class FlinsC6AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Flins C6 Elevated'
        self.Type = 'AttackEffect'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType in ['DirectLunarCharged', 'LunarCharged']:
            if self.Character.Constellation >= 6:
                if AttackingCharacter == self.Character:
                    AttackingCharacterStat['ElevatedMultiplier'] += 0.35
                
                if self.Game.Moonsign >= 2:
                    AttackingCharacterStat['ElevatedMultiplier'] += 0.1

        return AttackingCharacterStat, TargetedEnemyStat
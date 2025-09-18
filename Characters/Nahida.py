
from Game import Game
from .BaseCharacter import BaseCharacter

# 버프 체크리스트
# 궁 나히다 삼업의 정화 피증 (AttackEffect)                   (complete) 
# P1 온필드 원마 (Buff)                                      (complete) 
# P2 나히다 삼업의 정화 치확/피증 (AttackEffect)              (complete) 
# C1 적용수 (AttackEffect)                                   (complete) 
# C2 파티 격변 치명타, 달개화 치명타, 방깎 (AttackEffect)     (complete) 
# C4 나히다 원마 (Buff)                                      (complete) 

class NahidaClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, CatalyzeActive=False, C4Cnt=1):
        super().__init__(Game=Game,
                         Name='Nahida',
                         Weapon='Catalyst',
                         Element='Dendro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
        if Level == 90:
            self.BaseStat['BaseHP'] += 10360
            self.BaseStat['BaseATK'] += 299
            self.BaseStat['BaseDEF'] += 630
        elif Level == 100:
            self.BaseStat['BaseHP'] += 11096
            self.BaseStat['BaseATK'] += 366
            self.BaseStat['BaseDEF'] += 675
        else:
            raise ValueError
        self.BaseStat['EM'] += 115

        self.C4Cnt = 1
        self.CatalyzeActive = CatalyzeActive

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3

        self.Game.AddEffect(NahidaQAttackEffect(Game, self))
        self.Game.AddEffect(NahidaP1Buff(Game, self))
        self.Game.AddEffect(NahidaP2AttackEffect(Game, self))
        self.Game.AddEffect(NahidaC2Debuff(Game, self))
        self.Game.AddEffect(NahidaC2AttackEffect(Game, self))
        self.Game.AddEffect(NahidaC4Buff(Game, self, C4Cnt))
    
        
    def NA1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.725, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.856, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 1단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.666, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.786, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 2단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA3(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.826, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.975, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 3단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA4(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.051, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.241, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 4단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Charge(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.376, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.805, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Charge',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def C6Damage(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 2.00, 'DEF' : 0., 'EM' : 4.00}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 6돌 피해',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillPress(self, TargetedEnemy, Reaction=None, Print=True):
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.771, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.091, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 짧은터치',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillHold(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.347, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.771, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 홀드',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def TriKarmaPurification(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.858, 'DEF' : 0., 'EM' : 3.715}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.193, 'DEF' : 0., 'EM' : 4.386}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 삼업의 정화',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA1Combine(self, TargetedEnemy, Reaction=None, ReactionC6=None, Print=True):
        DMG = 0
        DMG += self.NA1(TargetedEnemy, Reaction, Print=False)
        if self.Constellation >= 6:
            DMG += self.C6Damage(TargetedEnemy, ReactionC6, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 1단 총합 피해 : {DMG}')
        return DMG
    
    def NA2Combine(self, TargetedEnemy, Reaction=None, ReactionC6=None, Print=True):
        DMG = 0
        DMG += self.NA2(TargetedEnemy, Reaction, Print=False)
        if self.Constellation >= 6:
            DMG += self.C6Damage(TargetedEnemy, ReactionC6, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 2단 총합 피해 : {DMG}')
        return DMG
    
    def NA3Combine(self, TargetedEnemy, Reaction=None, ReactionC6=None, Print=True):
        DMG = 0
        DMG += self.NA3(TargetedEnemy, Reaction, Print=False)
        if self.Constellation >= 6:
            DMG += self.C6Damage(TargetedEnemy, ReactionC6, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 3단 총합 피해 : {DMG}')
        return DMG
    
    def NA4Combine(self, TargetedEnemy, Reaction=None, ReactionC6=None, Print=True):
        DMG = 0
        DMG += self.NA4(TargetedEnemy, Reaction, Print=False)
        if self.Constellation >= 6:
            DMG += self.C6Damage(TargetedEnemy, ReactionC6, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 4단 총합 피해 : {DMG}')
        return DMG
    
    def ChargeCombine(self, TargetedEnemy, Reaction=None, ReactionC6=None, Print=True):
        DMG = 0
        DMG += self.Charge(TargetedEnemy, Reaction, Print=False)
        if self.Constellation >= 6:
            DMG += self.C6Damage(TargetedEnemy, ReactionC6, Print=False)

        if Print:
            print(f'{self.Name} 강공격 총합 피해 : {DMG}')
        return DMG
    
    def Rotation(self, TargetedEnemey, Count, Reaction=None):
        DMG = 0
        DMG += self.SkillPress(TargetedEnemey, Reaction=Reaction, Print=True)
        for i in range(Count):
            DMG += self.TriKarmaPurification(TargetedEnemey, Reaction=Reaction, Print=True)
        return DMG
    

class NahidaQAttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nahida Q Buff'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if '삼업의 정화' in AttackName:
                PyroCnt = 0
                for Character in self.Game.Characters:
                    if Character.Element == 'Pyro':
                        PyroCnt += 1

                if self.Character.Constellation >= 1:
                    PyroCnt += 1
            
                if PyroCnt == 1:
                    if self.Character.SkillLevel['Ult'] == 10:
                        AttackingCharacterStat['DMGBonus'] += 0.268
                    elif self.Character.SkillLevel['Ult'] == 13:
                        AttackingCharacterStat['DMGBonus'] += 0.316
                    else:
                        raise NotImplementedError
                elif PyroCnt >= 2:
                    if self.Character.SkillLevel['Ult'] == 10:
                        AttackingCharacterStat['DMGBonus'] += 0.402
                    elif self.Character.SkillLevel['Ult'] == 13:
                        AttackingCharacterStat['DMGBonus'] += 0.474
                    else:
                        raise NotImplementedError
                
        return AttackingCharacterStat, TargetedEnemyStat

class NahidaP1Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Nahida P1 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Game.OnField:
            Stat = 'EM'
            maxEM = 0

            for Character in self.Game.Characters:
                maxEM = max(maxEM, Character.BuffedStat['EM'])

            Amount = min(250, maxEM * 0.25)
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class NahidaP2AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nahida P2 Buff'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if '삼업의 정화' in AttackName:
                EM = self.Character.FinalStat['EM']
                AttackingCharacterStat['DMGBonus'] += min(0.80, (EM-200) * 0.001)   
                AttackingCharacterStat['CR'] += min(0.24, (EM-200) * 0.0003)
                
        return AttackingCharacterStat, TargetedEnemyStat

class NahidaC2Debuff: 
    def __init__(self, Game, Character):
        self.Name = 'Nahida C2 DefReduction'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character

    def Apply(self, DebuffedEnemy, Print):
        if self.Character.Constellation >= 2 and self.Character.CatalyzeActive:
            Stat = 'DEFReduction'
            Amount = 0.3
            DebuffedEnemy.DebuffedStat[Stat] += Amount
            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")

class NahidaC2AttackEffect:
    def __init__(self, Game, Character):
        self.Name = 'Nahida C2 Buff'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if self.Character.Constellation >= 2:
            if AttackType in ['Bloom', 'Hyperbloom','Burgeon', 'Burning']:
                AttackingCharacterStat['TransformativeCR'] += 0.2
                AttackingCharacterStat['TransformativeCD'] = max(AttackingCharacterStat['TransformativeCD'], 1.0)

            if AttackType == 'DirectLunarBloom':
                AttackingCharacterStat['CR'] += 0.1
                AttackingCharacterStat['CD'] += 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class NahidaC4Buff: 
    def __init__(self, Game, Character, Cnt):
        self.Name = 'Nahida C4 EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.EM = [100, 120, 140, 160]
    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.Character.Constellation >= 4:
                Stat = 'EM'
                Amount = self.EM[self.Character.C4Cnt-1]
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


from Game import Game
from .BaseCharacter import BaseCharacter

# 버프 체크리스트
# E 적 내성깍 (Debuff)                               (complete) 
# Q 파티격변 추가피해 (AttackEffect)                  (complete) 
# P1 파티격변 치명타 (AttackEffect)                   (complete) 
# P2 라우마 스킬피증 (AttackEffect)                   (complete) 
# P3 파티 달개화 피증 (AttackEffect)                  (complete) 
# C2 파티 Q추가피해 + 달개화 피증 (AttackEffect)       (complete) 
# C6 파티 달개화 승격(AttackEffect)                    (complete) 


class LaumaClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=0):
        super().__init__(Game=Game,
                         Name='Lauma',
                         Weapon='Catalyst',
                         Element='Dendro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)

        if Level == 90:
            self.BaseStat['BaseHP'] += 10654
            self.BaseStat['BaseATK'] += 255
            self.BaseStat['BaseDEF'] += 669
        elif Level == 100:
            self.BaseStat['BaseHP'] += 11411
            self.BaseStat['BaseATK'] += 312
            self.BaseStat['BaseDEF'] += 716
        else:
            raise ValueError
        self.BaseStat['EM'] += 315

        self.Game.Moonsign += 1

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3

        self.Game.AddEffect(LaumaEDebuff(Game, self))
        self.Game.AddEffect(LaumaQAttackEffect(Game, self))
        self.Game.AddEffect(LaumaP1AttackEffect(Game, self))
        self.Game.AddEffect(LaumaP2AttackEffect(Game, self))
        self.Game.AddEffect(LaumaP3AttackEffect(Game, self))
        self.Game.AddEffect(LaumaC6AttackEffect(Game, self))
        
    def NA1(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.607, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.716, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 1단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA2(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.572, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.676, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 2단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NA3(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.676, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.946, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 3단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def NAC6(self, TargetedEnemy, Reaction=None, Print=False):

        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.5}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 일반공격 6돌',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillPress(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.189, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.584, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 터치',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillHold1hit(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.845, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 3.359, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 홀드 1단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillHold2hit(self, TargetedEnemy, Stack, Reaction=None, Print=False):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 2.736 * Stack}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 3.230 * Stack}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 홀드 2단',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def FrostgroveSanctuary(self, TargetedEnemy, Reaction=None, Print=False):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.728, 'DEF' : 0., 'EM' : 3.456}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.040, 'DEF' : 0., 'EM' : 4.080}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 서리숲영역',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def FrostgroveSanctuaryC6(self, TargetedEnemy, Reaction=None, Print=False):

        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.85}

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 서리숲영역 6돌',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillHoldCombine(self, TargetedEnemy, Stack, Print=True):
        DMG = 0 
        DMG += self.SkillHold1hit(TargetedEnemy, None, Print=False)
        DMG += self.SkillHold2hit(TargetedEnemy, Stack, None, Print=False)

        if Print:
            print(f'{self.Name} 원소스킬 홀드 총합 피해 : {DMG}')
        return DMG
    
    def FrostgroveSanctuaryCombine(self, TargetedEnemy, Print=True):
        DMG = 0

        DMG += self.FrostgroveSanctuary(TargetedEnemy, None, Print=False)
        if self.Constellation >= 6:
            DMG += self.FrostgroveSanctuaryC6(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 서리숲영역 총합 피해 : {DMG}')
        return DMG
    
    def NA1Combine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.NA1(TargetedEnemy, None, Print=False)
        if self.Constellation >= 6:
            DMG += self.NAC6(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 1단 총합 피해 : {DMG}')
        return DMG
    
    def NA2Combine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.NA2(TargetedEnemy, None, Print=False)
        if self.Constellation >= 6:
            DMG += self.NAC6(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 2단 피해 : {DMG}')
        return DMG
    
    def NA3Combine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.NA3(TargetedEnemy, None, Print=False)
        if self.Constellation >= 6:
            DMG += self.NAC6(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 일반공격 3단 피해 : {DMG}')
        return DMG
    
    def Rotation(self, TargetedEnemy, EHold, Stack, Count):
        DMG = 0
        if EHold == True:
            DMG += self.SkillHoldCombine(TargetedEnemy, Stack, True)
        else:
            DMG += self.SkillPress(TargetedEnemy, None, True)
        
        for i in range(Count):
            DMG += self.FrostgroveSanctuaryCombine(TargetedEnemy, True)
        
        return DMG

class LaumaEDebuff: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma E Res'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, DebuffedEnemy, Print):
        Stat1 = 'DendroRes'
        Stat2 = 'HydroRes'

        if self.Character.SkillLevel['Skill'] == 10:
            Amount = -0.25
        elif self.Character.SkillLevel['Skill'] == 13:
            Amount = -0.34
        else:
            raise NotImplementedError

        DebuffedEnemy.DebuffedStat[Stat1] += Amount
        DebuffedEnemy.DebuffedStat[Stat2] += Amount
        if Print:
            print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat1:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat1]:<5.3f}")
            print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat2:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat2]:<5.3f}")



class LaumaQAttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma Q DMGBonus'
        self.Type = 'AttackEffect'

        self.Game=Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        EM = self.Character.FinalStat['EM']
        if AttackType in ['Bloom', 'Hyperbloom','Burgeon']:

            if self.Character.SkillLevel['Ult'] == 10:
                Multiplier = 5.0
            elif self.Character.SkillLevel['Ult'] == 13:
                Multiplier = 5.902
            else:
                raise NotImplementedError
            
            if self.Character.Constellation >= 2:
                Multiplier += 5.0

            AttackingCharacterStat['AdditiveBaseDMGBonus'] += EM * Multiplier
        
        if AttackType == 'DirectLunarBloom':

            if self.Character.SkillLevel['Ult'] == 10:
                Multiplier = 4.0
            elif self.Character.SkillLevel['Ult'] == 13:
                Multiplier = 4.723
            else:
                raise NotImplementedError

            if self.Character.Constellation >= 2:
                Multiplier += 4.0
                if self.Game.Moonsign >= 2:
                    AttackingCharacterStat['ReactionBonus'] += 0.4
                
            AttackingCharacterStat['AdditiveBaseDMGBonus'] += EM * Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat
    

class LaumaP1AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P1 Crit'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if self.Game.Moonsign == 1:
            if AttackType in ['Bloom', 'Hyperbloom','Burgeon']:
                AttackingCharacterStat['TransformativeCR'] += 0.15
                AttackingCharacterStat['TransformativeCD'] = max(AttackingCharacterStat['TransformativeCD'], 1.0)

        if self.Game.Moonsign >= 2:
            if AttackType == 'DirectLunarBloom':
                AttackingCharacterStat['CR'] += 0.1
                AttackingCharacterStat['CD'] += 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class LaumaP2AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P2 E DMGBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        
        if AttackingCharacter == self.Character:
            EM = self.Character.FinalStat['EM']
            DMGBonus = min(0.32, 0.0004 * EM)

            if DMGType == 'Skill':
                AttackingCharacterStat['DMGBonus'] += DMGBonus

        return AttackingCharacterStat, TargetedEnemyStat
    
class LaumaP3AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P3 LunarBloomDMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType == 'DirectLunarBloom':
            EM = self.Character.FinalStat['EM'] 
            Amount = min(0.14, EM * 0.000175)
            
            AttackingCharacterStat['LunarBloomBaseDMGBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat

    
class LaumaC6AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma C6 Elevated'
        self.Type = 'AttackEffect'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType == 'DirectLunarBloom':
            if self.Character.Constellation >= 6:
                AttackingCharacterStat['ElevatedMultiplier'] += 0.25

        return AttackingCharacterStat, TargetedEnemyStat
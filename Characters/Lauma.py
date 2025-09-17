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
    def __init__(self, Game : Game, Level, SkillLevel, Constellation, Moonsign):
        self.Name = 'Lauma'
        self.Element = 'Dendro'
        self.Game = Game

        if Level == 90:
            BaseHP = 10654
            BaseATK = 255
            BaseDEF = 669
        elif Level == 100:
            BaseHP = 11411
            BaseATK = 312
            BaseDEF = 716
        else:
            raise ValueError

        self.BaseStat = {
            'Level' : Level,
            'BaseHP' : BaseHP,
            'BaseATK' : BaseATK,
            'BaseDEF' : BaseDEF,
            '%HP' : 0,
            '%ATK' : 0,
            '%DEF' : 0,
            'AdditiveHP' : 0,
            'AdditiveATK' : 0,
            'AdditiveDEF' : 0,
            'EM' : 315,
            'ER' : 1.0,
            'CR' : 0.05,
            'CD' : 0.5,
            'BaseDMGMultiplier' : 0, # 곱연산 피증 (ex,느비 특성) (버프 계산시 100% 뺴야함)
            'AdditiveBaseDMGBonus' : 0,
            'PhysicalDMGBonus' : 0,
            'AnemoDMGBonus' : 0,
            'GeoDMGBonus' : 0,
            'ElectroDMGBonus' : 0,
            'DendroDMGBonus' : 0,
            'HydroDMGBonus' : 0,
            'PyroDMGBonus' : 0,
            'CyroDMGBonus' : 0,
            'DMGBonus' : 0,
            'ReactionBonus' : 0,
            'DEFIgnored' : 0,
            'LunarChargedBaseDMGBonus' : 0,
            'LunarBloomBaseDMGBonus' : 0,
            'ElevatedMultiplier' : 0, # 승격(버프 계산시 100% 뺴야함)
            'TransformativeCR' : 0,
            'TransformativeCD' : 0
        }
        assert Moonsign in [1, 2]
        self.Moonsign = Moonsign
        self.SkillLevel = SkillLevel
        self.Constellation = Constellation

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

        self.TotalDamageDealt = 0
        
    def NA1(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 일반공격 1단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.607, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.716, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def NA2(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 일반공격 2단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.572, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.676, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def NA3(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 일반공격 3단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.676, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.946, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def NAC6(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 일반공격 6돌'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.5}

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillPress(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 원소스킬 터치'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Skill'
        DMGType = 'Skill'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.189, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.584, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillHold1hit(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 원소스킬 홀드 1단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Skill'
        DMGType = 'Skill'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 2.845, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 3.359, 'DEF' : 0., 'EM' : 0}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillHold2hit(self, TargetedEnemy, Stack, Reaction=None, Print=False):
        AttackName = f'{self.Name} 원소스킬 홀드 2단'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 2.736 * Stack}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 3.230 * Stack}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def FrostgroveSanctuary(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 서리숲영역'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Skill'
        DMGType = 'Skill'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.728, 'DEF' : 0., 'EM' : 3.456}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 2.040, 'DEF' : 0., 'EM' : 4.080}
        else:
            raise NotImplementedError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def FrostgroveSanctuaryC6(self, TargetedEnemy, Reaction=None, Print=False):
        AttackName = f'{self.Name} 서리숲영역 6돌'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.85}

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillHoldCombine(self, TargetedEnemy, Stack, Print=True):
        DMG = 0 
        DMG += self.SkillHold1hit(TargetedEnemy, None, Print=False)
        DMG += self.SkillHold2hit(TargetedEnemy, Stack, None, Print=False)

        if Print:
            print(f'{self.Name} 원소스킬 홀드 총합 피해 : {DMG}')
        return DMG
    
    def FrostgroveSanctuaryCombine(self, TargetedEnemy, Count, Print=True):
        DMG = 0

        for i in range(Count):
            DMG += self.FrostgroveSanctuary(TargetedEnemy, None, Print=False)
            if self.Constellation >= 6:
                DMG += self.FrostgroveSanctuaryC6(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 서리숲영역 {Count}회 총합 피해 : {DMG}')
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

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
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
                if self.Character.Moonsign == 2:
                    AttackingCharacterStat['ReactionBonus'] += 0.4
                
            AttackingCharacterStat['AdditiveBaseDMGBonus'] += EM * Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat
    

class LaumaP1AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P1 Crit'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.Character.Moonsign == 1:
            if AttackType in ['Bloom', 'Hyperbloom','Burgeon']:
                AttackingCharacterStat['TransformativeCR'] += 0.15
                AttackingCharacterStat['TransformativeCD'] = max(AttackingCharacterStat['TransformativeCD'], 1.0)

        if self.Character.Moonsign == 2:
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

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        
        if AttackingCharacter == self.Character:
            EM = self.Character.FinalStat['EM']
            DMGBonus = min(0.32, 0.0004 * EM)

            if SkillType == 'Skill':
                AttackingCharacterStat['DMGBonus'] += DMGBonus

        return AttackingCharacterStat, TargetedEnemyStat
    
class LaumaP3AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P3 LunarBloomDMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
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

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if AttackType == 'DirectLunarBloom':
            if self.Character.Constellation >= 6:
                AttackingCharacterStat['ElevatedMultiplier'] += 0.25

        return AttackingCharacterStat, TargetedEnemyStat
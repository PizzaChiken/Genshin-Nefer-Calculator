
from Game import Game

class NeferClass:
    def __init__(self, Game : Game, Level = 90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0):
        self.Name = 'Nefer'
        self.Element = 'Dendro'
        self.Game = Game

        if Level == 90:
            BaseHP = 12704
            BaseATK = 344
            BaseDEF = 799
        elif Level == 100:
            BaseHP = 13607
            BaseATK = 422
            BaseDEF = 856
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
            'EM' : 200,
            'ER' : 1.0,
            'CR' : 0.05,
            'CD' : 0.884,
            'BaseDMGMultiplier' : 0,
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
            'ElevatedMultiplier' : 1.0 # 승격(버프 계산시 100% 뺴야함)
        }

        self.SkillLevel = SkillLevel
        self.Constellation = Constellation

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3


        self.Game.AddEffect(NeferUltAttackEffect(self))
        self.Game.AddEffect(NeferP1EMBuff(self))
        self.Game.AddEffect(NeferP1MultiplierAttackEffect(self))
        self.Game.AddEffect(NeferP3Buff(self))
        self.Game.AddEffect(NeferC4AttackEffect(self))
        self.Game.AddEffect(NeferP2Buff(self))
        self.Game.AddEffect(NeferC6AttackEffect(self))
        
    
    def initBuffedStat(self):
        self.BuffedStat = self.BaseStat.copy()
    
    def AddWeapon(self, Weapon):
        for Stat in Weapon.StatList.keys():
            self.BaseStat[Stat] += Weapon.StatList[Stat]
        for Effect in Weapon.EffectList:
            self.Game.AddEffect(Effect)
    
    def AddArtifactSet(self, ArtifactSet):
        for Stat in ArtifactSet.StatList.keys():
            self.BaseStat[Stat] +=  ArtifactSet.StatList[Stat]
        for Effect in ArtifactSet.EffectList:
            self.Game.AddEffect(Effect)
    
    def AddArtifacts(self, Artifacts):
        for Artifact in Artifacts:
            for Stat in Artifact.keys():
                self.BaseStat[Stat] += Artifact[Stat]

    def DisplayBaseStat(self):
        print(f'{self.Name} Level            : {self.BaseStat['Level']}')
        print(f'{self.Name} HP               : {self.BaseStat['BaseHP'] * (1 + self.BaseStat['%HP']) + self.BaseStat['AdditiveHP']}')
        print(f'{self.Name} ATK              : {self.BaseStat['BaseATK'] * (1 + self.BaseStat['%ATK']) + self.BaseStat['AdditiveATK']}')
        print(f'{self.Name} DEF              : {self.BaseStat['BaseDEF'] * (1 + self.BaseStat['%DEF']) + self.BaseStat['AdditiveDEF']}')
        print(f'{self.Name} EM               : {self.BaseStat['EM']}')
        print(f'{self.Name} ER               : {self.BaseStat['ER']}')
        print(f'{self.Name} CR               : {self.BaseStat['CR']}')
        print(f'{self.Name} CD               : {self.BaseStat['CD']}')
        print(f'{self.Name} ElementalDMGBonus: {self.BaseStat[f'{self.Element}DMGBonus']}')
        print(f'{self.Name} DMGBonus         : {self.BaseStat[f'DMGBonus']}')
        print('\n')
        print(self.BaseStat)
        print('\n')

        
    def NA1(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '일반공격 1단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.685, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.809, 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillInit(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '원소스킬 시전'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.375, 'DEF' : 0., 'EM' : 2.75}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCANefer1(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (네페르) 1단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Charge'
        DMGType = 'Charge'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.444, 'DEF' : 0., 'EM' : 0.887}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.524, 'DEF' : 0., 'EM' : 1.047}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG

    def SkillCANefer2(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (네페르) 2단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Charge'
        DMGType = 'Charge'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.577, 'DEF' : 0., 'EM' : 1.153}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.681, 'DEF' : 0., 'EM' : 1.361}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCANefer2C6(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (네페르) 2단 6돌'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 0.85}

        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCAShade1(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (환영) 1단'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.728}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.04}
        else:
            raise ValueError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCAShade2(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (환영) 2단'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.728}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.04}
        else:
            raise ValueError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCAShade3(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 (환영) 3단'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.304}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 2.72}
        else:
            raise ValueError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCAFinalC6(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '환희 6돌 추가'
        AttackType = 'DirectLunarBloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.2}
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def Ult1(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '원소폭발 1단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Ult'
        DMGType = 'Ult'
        
        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 4.044, 'DEF' : 0., 'EM' : 8.087}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 4.774, 'DEF' : 0., 'EM' : 9.547}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def Ult2(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '원소폭발 2단'
        AttackType = 'Basic'
        AttackElement = 'Dendro'
        SkillType = 'Ult'
        DMGType = 'Ult'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 6.605, 'DEF' : 0., 'EM' : 12.131}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 7.160, 'DEF' : 0., 'EM' : 14.321}
        else:
            raise ValueError

        AttackingCharacterStat = self.BuffedStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
        return DMG
    
    def SkillCACombine(self, TargetedEnemy, Reaction=None, Print=True):
        BasicDMG = 0
        LunarBloomDmg = 0

        BasicDMG += self.SkillCANefer1(TargetedEnemy, Reaction, Print=False)

        if self.Constellation >= 6:
            LunarBloomDmg += self.SkillCANefer2C6(TargetedEnemy, Reaction, Print=False)
        else:
            BasicDMG += self.SkillCANefer2(TargetedEnemy, Reaction, Print=False)
            
        LunarBloomDmg += self.SkillCAShade1(TargetedEnemy, Reaction, Print=False)
        LunarBloomDmg += self.SkillCAShade2(TargetedEnemy, Reaction, Print=False)
        LunarBloomDmg += self.SkillCAShade3(TargetedEnemy, Reaction, Print=False)

        if self.Constellation >= 6:
            LunarBloomDmg += self.SkillCAFinalC6(TargetedEnemy, Reaction, Print=False)
        
        FinalDMG = BasicDMG + LunarBloomDmg
        
        if Print:
            print(f'{self.Name} 환상극 피해 -> 일반 : {BasicDMG}, 달개화 : {LunarBloomDmg}, 총합 : {FinalDMG}')
        return FinalDMG
    
    def UltCombine(self, TargetedEnemy, Reaction=None, Print=True):
        DMG = 0 
        DMG += self.Ult1(TargetedEnemy, Reaction, Print=False)
        DMG += self.Ult2(TargetedEnemy, Reaction, Print=False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG

# 개인버프

class NeferUltAttackEffect: 
    def __init__(self, Character):
        self.Name = 'Nefer Ult DMGMultiplier'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):

        if AttackingCharacter == self.Character:
            if '원소폭발' in AttackName:
                if self.Character.SkillLevel['Ult'] == 10:
                    Multiplier = 0.4
                elif self.Character.SkillLevel['Ult'] == 13:
                    Multiplier = 0.49
                else:
                    raise ValueError

                if self.Character.Constellation >= 2:
                    stack = 5
                else:
                    stack = 3
                AttackingCharacterStat['BaseDMGMultiplier'] += Multiplier * stack
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class NeferP1EMBuff: # (범용상황, 범용버프) + (범용상황, 특정버프) + (특정상황, 특정버프) 
    def __init__(self, Character):
        self.Name = 'Nefer P1 EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat = 'EM'
            Amount = 200 if self.Character.Constellation >= 2 else 100
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


class NeferP1MultiplierAttackEffect: 
    def __init__(self, Character):
        self.Name = 'Nefer P1 CA DMGMultiplier'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        
    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if AttackingCharacter == self.Character:
            if '환희' in AttackName:
                Multiplier = 0.5 if self.Character.Constellation >= 2 else 0.3
                AttackingCharacterStat['BaseDMGMultiplier'] += Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat
    
    
class NeferP3Buff: 
    def __init__(self, Character):
        self.Name = 'Nefer P3 ATK Bonus'
        self.Proportional = True
        self.Type = 'Buff'

        self.Character = Character
    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat = 'AdditiveATK'

            EM = self.Character.BuffedStat['EM']
            Amount = min(200, (EM - 500) * 0.4) if EM >= 500 else 0

            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

    
class NeferC4AttackEffect: 
    def __init__(self, Character):
        self.Name = 'Nefer C4 Res'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if AttackingCharacter == self.Character:
            if self.Character.Constellation >= 4:
                TargetedEnemyStat['DendroRes'] -= 0.2
            
        return AttackingCharacterStat, TargetedEnemyStat



# 파티버프
    
class NeferP2Buff: 
    def __init__(self, Character=None, EM=None):
        self.Name = 'Nefer P2 LunarBloomDMG'
        self.Proportional = True
        self.Type = 'Buff'

        self.Character = Character
        self.EM = EM


    def Apply(self, BuffedCharacter, Print):
        Stat = 'LunarBloomBaseDMGBonus'

        EM = self.Character.BuffedStat['EM'] if self.Character is not None else self.EM
        Amount = min(0.14, EM * 0.000175)

        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


class NeferC6AttackEffect: 
    def __init__(self, Character=None, Constellation=6):
        self.Name = 'Nefer C6 Elevated'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Constellation = Constellation

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if 'LunarBloom' in AttackType:
            Constellation = self.Character.Constellation if self.Character is not None else self.Constellation
            if Constellation >= 6:
                AttackingCharacterStat['ElevatedMultiplier'] += 0.15

        return AttackingCharacterStat, TargetedEnemyStat
    
def AddNeferTemp(Game, Constellation, EM):
    Game.AddEffect(NeferP2Buff(EM=EM))
    Game.AddEffect(NeferC6AttackEffect(Constellation=Constellation))
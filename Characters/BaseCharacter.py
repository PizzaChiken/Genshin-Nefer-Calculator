
from Game import Game

class BaseCharacter:
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0):
        self.Name = '네페르'
        self.Element = 'Dendro'
        self.Game = Game

        if Level == 90:
            BaseHP = 0
            BaseATK = 0
            BaseDEF = 0
        elif Level == 100:
            BaseHP = 0
            BaseATK = 0
            BaseDEF = 0
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
            'EM' : 0,
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
        
        self.SkillLevel = SkillLevel
        self.Constellation = Constellation
        
        self.Game.AddEffect(BasicBuff(Game, self))
        self.Game.AddEffect(BasicDebuff(Game, self))
        self.Game.AddEffect(BasicAttackEffect(Game, self))

        self.TotalDamageDealt = 0
    
    def initBuffedStat(self):
        # 비례버프 아닌 스택 적용
        self.BuffedStat = self.BaseStat.copy()
    
    def initFinalStat(self):
        # 비례버프 받은 뒤 최종 스탯
        self.FinalStat = self.BuffedStat.copy()
    
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
        print(f'{self.Name} HP               : {self.BaseStat['BaseHP'] * (1 + self.BaseStat['%HP']) + self.BaseStat['AdditiveHP']:.0f}')
        print(f'{self.Name} ATK              : {self.BaseStat['BaseATK'] * (1 + self.BaseStat['%ATK']) + self.BaseStat['AdditiveATK']:.0f}')
        print(f'{self.Name} DEF              : {self.BaseStat['BaseDEF'] * (1 + self.BaseStat['%DEF']) + self.BaseStat['AdditiveDEF']:.0f}')
        print(f'{self.Name} EM               : {self.BaseStat['EM']:.0f}')
        print(f'{self.Name} ER               : {self.BaseStat['ER']*100:.0f}%')
        print(f'{self.Name} CR               : {self.BaseStat['CR']*100:.0f}%')
        print(f'{self.Name} CD               : {self.BaseStat['CD']*100:.0f}%')
        print(f'{self.Name} ElementalDMGBonus: {self.BaseStat[f'{self.Element}DMGBonus']*100:.0f}%')
        print(f'{self.Name} DMGBonus         : {self.BaseStat[f'DMGBonus']*100:.0f}%')
        print('\n')

    def DisplayBuffedStat(self):
        print(f'{self.Name} Level            : {self.BuffedStat['Level']}')
        print(f'{self.Name} HP               : {self.BuffedStat['BaseHP'] * (1 + self.BuffedStat['%HP']) + self.BuffedStat['AdditiveHP']:.0f}')
        print(f'{self.Name} ATK              : {self.BuffedStat['BaseATK'] * (1 + self.BuffedStat['%ATK']) + self.BuffedStat['AdditiveATK']:.0f}')
        print(f'{self.Name} DEF              : {self.BuffedStat['BaseDEF'] * (1 + self.BuffedStat['%DEF']) + self.BuffedStat['AdditiveDEF']:.0f}')
        print(f'{self.Name} EM               : {self.BuffedStat['EM']:.0f}')
        print(f'{self.Name} ER               : {self.BuffedStat['ER']*100:.0f}%')
        print(f'{self.Name} CR               : {self.BuffedStat['CR']*100:.0f}%')
        print(f'{self.Name} CD               : {self.BuffedStat['CD']*100:.0f}%')
        print(f'{self.Name} ElementalDMGBonus: {self.BuffedStat[f'{self.Element}DMGBonus']*100:.0f}%')
        print(f'{self.Name} DMGBonus         : {self.BuffedStat[f'DMGBonus']*100:.0f}%')
        print('\n')

    def DisplayFinalStat(self):
        print(self.FinalStat['BaseHP'], self.FinalStat['%HP'], self.FinalStat['AdditiveHP'])
        print(f'{self.Name} Level            : {self.FinalStat['Level']}')
        print(f'{self.Name} HP               : {self.FinalStat['BaseHP'] * (1 + self.FinalStat['%HP']) + self.FinalStat['AdditiveHP']:.0f}')
        print(f'{self.Name} ATK              : {self.FinalStat['BaseATK'] * (1 + self.FinalStat['%ATK']) + self.FinalStat['AdditiveATK']:.0f}')
        print(f'{self.Name} DEF              : {self.FinalStat['BaseDEF'] * (1 + self.FinalStat['%DEF']) + self.FinalStat['AdditiveDEF']:.0f}')
        print(f'{self.Name} EM               : {self.FinalStat['EM']:.0f}')
        print(f'{self.Name} ER               : {self.FinalStat['ER']*100:.0f}%')
        print(f'{self.Name} CR               : {self.FinalStat['CR']*100:.0f}%')
        print(f'{self.Name} CD               : {self.FinalStat['CD']*100:.0f}%')
        print(f'{self.Name} ElementalDMGBonus: {self.FinalStat[f'{self.Element}DMGBonus']*100:.0f}%')
        print(f'{self.Name} DMGBonus         : {self.FinalStat[f'DMGBonus']*100:.0f}%')
        print('\n')

        
    def Damage(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 일반공격 1단'
        AttackType = 'Basic'
        AttackElement = 'Pyro'
        SkillType = 'Normal'
        DMGType = 'Normal'
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG

    def Bloom(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 개화'
        AttackType = 'Bloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG

    def Burgeon(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 발화'
        AttackType = 'Burgeon'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def Hyperbloom(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 만개'
        AttackType = 'Hyperbloom'
        AttackElement = 'Dendro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def Burning(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 연소'
        AttackType = 'Burning'
        AttackElement = 'Pyro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG

    def Overloaded(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 과부하'
        AttackType = 'Overloaded'
        AttackElement = 'Pyro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def ElectroCharged(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 감전'
        AttackType = 'ElectroCharged'
        AttackElement = 'Electro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def LunarCharged(self, TargetedEnemy, Reaction=None):
        AttackName = f'{self.Name} 달감전'
        AttackType = 'LunarCharged'
        AttackElement = 'Electro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        return DMG
    
    def Superconduct(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 초전도'
        AttackType = 'Superconduct'
        AttackElement = 'Cyro'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def Swirl(self, TargetedEnemy, Element, Reaction=None, Print=True):
        AttackName = f'{self.Name} 확산'
        AttackType = 'Swirl'
        AttackElement = Element
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG
    
    def Shatter(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = f'{self.Name} 쇄빙'
        AttackType = 'Shatter'
        AttackElement = 'Physical'
        SkillType = None
        DMGType = None
        
        Multiplier = None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

        DMG = self.Game.ApplyDMG(AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG

# 특정 상황 : LunarBloomDamage, LunarChargedDamage, ...
# 특정 버프 : LunarBloomBaseDMGBonus, ...
# 범용 상황 : BasicDamage ,...
# 범용 버프 : ATK, EM, ...

class BasicBuff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Basic버프'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        Stat = ''
        Amount = 0
        BuffedCharacter.BuffedStat[Stat] += Amount  
        # self.Proportional = True 일경우 
        # BuffedCharacter.FinalStat[Stat] += Amount
        if Print:
            print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            # self.Proportional = True 일경우 
            #print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")


class BasicDebuff: # (범용상황, 범용버프) 
    def __init__(self, Game, Character):
        self.Name = 'Basic디버프'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character

    def Apply(self, DebuffedEnemy, Print):
        Stat = ''
        Amount = 0
        DebuffedEnemy.DebuffedStat[Stat] += Amount
        if Print:
             print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")


class BasicAttackEffect: # (특정상황, 범용버프) + (범용상황, 특정버프) + (특정상황, 특정버프) 
    def __init__(self, Game, Character):
        self.Name = 'Basic공격효과'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        
        return AttackingCharacterStat, TargetedEnemyStat
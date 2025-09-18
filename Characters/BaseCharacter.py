
from Game import Game

class BaseCharacter:
    def __init__(self, Game:Game, Name, Weapon, Element, Level, SkillLevel, Constellation):
        self.Game = Game
        self.Name = Name
        self.Weapon = Weapon
        self.Element = Element

        self.BaseStat = {
            'Level' : Level,

            'BaseHP' : 0,
            'BaseATK' : 0,
            'BaseDEF' : 0,

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

            'NormalDMGBonus' : 0,
            'ChargeDMGBonus' : 0,
            'PlungingDMGBonus' : 0,
            'SkillDMGBonus' : 0,
            'UltDMGBonus' : 0,

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
    
    @property 
    def BaseHP(self) : return self.BaseStat['BaseHP'] * (1 + self.BaseStat['%HP']) + self.BaseStat['AdditiveHP']
    @property 
    def BaseATK(self) : return self.BaseStat['BaseATK'] * (1 + self.BaseStat['%ATK']) + self.BaseStat['AdditiveATK'] 
    @property 
    def BaseDEF(self) : return self.BaseStat['BaseDEF'] * (1 + self.BaseStat['%DEF']) + self.BaseStat['AdditiveDEF']
    @property
    def BuffedHP(self) : return self.BuffedStat['BaseHP'] * (1 + self.BuffedStat['%HP']) + self.BuffedStat['AdditiveHP']
    @property
    def BuffedATK(self) : return self.BuffedStat['BaseATK'] * (1 + self.BuffedStat['%ATK']) + self.BuffedStat['AdditiveATK'] 
    @property 
    def BuffedDEF(self) : return self.BuffedStat['BaseDEF'] * (1 + self.BuffedStat['%DEF']) + self.BuffedStat['AdditiveDEF']
    @property 
    def FinalHP(self) : return self.FinalStat['BaseHP'] * (1 + self.FinalStat['%HP']) + self.FinalStat['AdditiveHP']
    @property 
    def FinalATK(self) : return self.FinalStat['BaseATK'] * (1 + self.FinalStat['%ATK']) + self.FinalStat['AdditiveATK'] 
    @property 
    def FinalDEF(self) : return self.FinalStat['BaseDEF'] * (1 + self.FinalStat['%DEF']) + self.FinalStat['AdditiveDEF']


    def DisplayBaseStat(self):
        print(f'{self.Name:8} {'Level':30} : {self.BaseStat['Level']}')
        print(f'{self.Name:8} {'HP':30} : {self.BaseHP:.0f}')
        print(f'{self.Name:8} {'ATK':30} : {self.BaseATK:.0f}')
        print(f'{self.Name:8} {'DEF':30} : {self.BaseDEF:.0f}')
        print(f'{self.Name:8} {'EM':30} : {self.BaseStat['EM']:.0f}')
        for key in self.BaseStat.keys():
            if key not in ['Level', 'BaseHP', 'BaseATK', 'BaseDEF', '%HP', '%ATK', '%DEF', 'AdditiveHP', 'AdditiveATK', 'AdditiveDEF', 'EM']:
                print(f'{self.Name:8} {key:20} : {self.BaseStat[key]*100:.0f}%')

    def DisplayBuffedStat(self):
        print(f'{self.Name:8} {'Level':30} : {self.BuffedStat['Level']}')
        print(f'{self.Name:8} {'HP':30} : {self.BuffedHP:.0f}')
        print(f'{self.Name:8} {'ATK':30} : {self.BuffedATK:.0f}')
        print(f'{self.Name:8} {'DEF':30} : {self.BuffedDEF:.0f}')
        print(f'{self.Name:8} {'EM':30} : {self.BuffedStat['EM']:.0f}')
        for key in self.BuffedStat.keys():
            if key not in ['Level', 'BaseHP', 'BaseATK', 'BaseDEF', '%HP', '%ATK', '%DEF', 'AdditiveHP', 'AdditiveATK', 'AdditiveDEF', 'EM']:
                print(f'{self.Name:8} {key:30} : {self.BuffedStat[key]*100:.0f}%')

    def DisplayFinalStat(self):
        print(f'{self.Name:8} {'Level':30} : {self.FinalStat['Level']}')
        print(f'{self.Name:8} {'HP':30} : {self.FinalHP:.0f}')
        print(f'{self.Name:8} {'ATK':30} : {self.FinalATK:.0f}')
        print(f'{self.Name:8} {'DEF':30} : {self.FinalDEF:.0f}')
        print(f'{self.Name:8} {'EM':30} : {self.FinalStat['EM']:.0f}')
        for key in self.FinalStat.keys():
            if key not in ['Level', 'BaseHP', 'BaseATK', 'BaseDEF', '%HP', '%ATK', '%DEF', 'AdditiveHP', 'AdditiveATK', 'AdditiveDEF', 'EM']:
                print(f'{self.Name:8} {key:30} : {self.FinalStat[key]*100:.0f}%')
        print('\n')

        
    def Damage(self,
               TargetedEnemy,
               Reaction,
               AttackName,
               AttackType,
               AttackElement,
               DMGType,
               Multiplier,
               Print):
        
        assert AttackElement in ['Physical', 'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cyro']
        assert Reaction in [None, '촉진', '발산', '융해', '증발']
        assert AttackType in ['Basic', 
                              'DirectLunarCharged', 
                              'DirectLunarBloom', 
                              'Bloom', 
                              'Burgeon', 
                              'Hyperbloom', 
                              'Burning', 
                              'Overloaded',
                              'ElectroCharged',
                              'LunarCharged',
                              'Superconduct',
                              'Swirl',
                              'Shatter']
        assert DMGType in [None, 'Normal', 'Charge', 'Plunging', 'Skill', 'Ult']
        if AttackType != 'Basic':
            assert DMGType == Reaction == None
        if AttackType not in ['Basic', 'DirectLunarCharged', 'DirectLunarBloom']:
            assert Multiplier == None

        AttackingCharacterStat = self.FinalStat.copy()
        TargetedEnemyStat = TargetedEnemy.DebuffedStat.copy()

        AttackingCharacterStat, TargetedEnemyStat = self.Game.ApplyAttackEffect(self, 
                                                                                TargetedEnemy, 
                                                                                AttackingCharacterStat, 
                                                                                TargetedEnemyStat, 
                                                                                AttackName, 
                                                                                AttackElement, 
                                                                                Reaction, 
                                                                                AttackType, 
                                                                                DMGType)

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, 
                                 TargetedEnemyStat, 
                                 AttackElement, 
                                 Reaction, 
                                 AttackType, 
                                 DMGType,
                                 Multiplier)
        
        if AttackType != 'LunarCharged':
            self.TotalDamageDealt += DMG

        if Print:
            print(f'{AttackName} 피해 : {DMG}')
        return DMG

    def Bloom(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 개화',
                           AttackType = 'Bloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)

    def Burgeon(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 발화',
                           AttackType = 'Burgeon',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)

    
    def Hyperbloom(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 만개',
                           AttackType = 'Hyperbloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)
    
    def Burning(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 연소',
                           AttackType = 'Burning',
                           AttackElement = 'Pyro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)

    def Overloaded(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 과부하',
                           AttackType = 'Overloaded',
                           AttackElement = 'Pyro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)
    
    def ElectroCharged(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 감전',
                           AttackType = 'ElectroCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)
    
    def LunarCharged(self, TargetedEnemy):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 달감전',
                           AttackType = 'LunarCharged',
                           AttackElement = 'Electro',
                           DMGType = None,
                           Multiplier = None,
                           Print=False)
    
    def Superconduct(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 초전도',
                           AttackType = 'Superconduct',
                           AttackElement = 'Cyro',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)
    
    def Swirl(self, TargetedEnemy, Element, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 확산',
                           AttackType = 'Swirl',
                           AttackElement = Element,
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)
    
    def Shatter(self, TargetedEnemy, Print=True):
        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=None,
                           AttackName = f'{self.Name} 쇄빙',
                           AttackType = 'Shatter',
                           AttackElement = 'Physical',
                           DMGType = None,
                           Multiplier = None,
                           Print=Print)

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

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        
        return AttackingCharacterStat, TargetedEnemyStat
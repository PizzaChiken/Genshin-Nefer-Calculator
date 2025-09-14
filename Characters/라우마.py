from Game import Game

class LaumaClass:
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
            'ElevatedMultiplier' : 1.0 # 승격(버프 계산시 100% 뺴야함)
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
        self.Game.AddEffect(LaumaP3Buff(Game, self))
        self.Game.AddEffect(LaumaC6AttackEffect(Game, self))
    
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

    def DisplayFinalStat(self):
        print(f'{self.Name} Level            : {self.FinalStat['Level']}')
        print(f'{self.Name} HP               : {self.FinalStat['BaseHP'] * (1 + self.FinalStat['%HP']) + self.FinalStat['AdditiveHP']}')
        print(f'{self.Name} ATK              : {self.FinalStat['BaseATK'] * (1 + self.FinalStat['%ATK']) + self.FinalStat['AdditiveATK']}')
        print(f'{self.Name} DEF              : {self.FinalStat['BaseDEF'] * (1 + self.FinalStat['%DEF']) + self.FinalStat['AdditiveDEF']}')
        print(f'{self.Name} EM               : {self.FinalStat['EM']}')
        print(f'{self.Name} ER               : {self.FinalStat['ER']}')
        print(f'{self.Name} CR               : {self.FinalStat['CR']}')
        print(f'{self.Name} CD               : {self.FinalStat['CD']}')
        print(f'{self.Name} ElementalDMGBonus: {self.FinalStat[f'{self.Element}DMGBonus']}')
        print(f'{self.Name} DMGBonus         : {self.FinalStat[f'DMGBonus']}')
        print('\n')
        print(self.FinalStat)
        print('\n')
        
    def Damage(self, TargetedEnemy, Reaction=None, Print=True):
        AttackName = '일반공격 1단'
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

        DMG = self.Game.ApplyDMG(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        if Print:
            print(f'{self.Name} {AttackName} 피해 : {DMG}')
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
        # 개화 반응 NotImplemented
        
        if 'LunarBloom' in AttackType:
            
            EM = self.Character.FinalStat['EM']

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
        self.Name1 = 'Lauma P1 Crit'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.Character.Moonsign == 1:
            raise NotImplementedError
        if self.Character.Moonsign == 2:
            if 'LunarBloom' in AttackType:
                AttackingCharacterStat['CR'] + 0.1
                AttackingCharacterStat['CD'] + 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class LaumaP2AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P2 E DMGBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        # 개화 반응 NotImplemented
        
        if AttackingCharacter == self.Character:
            EM = self.Character.FinalStat['EM']
            DMGBonus = min(0.32, 0.0004 * EM)

            if SkillType == 'Skill':
                AttackingCharacterStat['DMGBonus'] += DMGBonus

        return AttackingCharacterStat, TargetedEnemyStat
    
class LaumaP3Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma P3 LunarBloomDMG'
        self.Proportional = True
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character
        
    def Apply(self, BuffedCharacter, Print):
        Stat = 'LunarBloomBaseDMGBonus'

        EM = self.Character.BuffedStat['EM'] 
        Amount = min(0.14, EM * 0.000175)

        BuffedCharacter.FinalStat[Stat] += Amount

        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

    
class LaumaC6AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Lauma C6 Elevated'
        self.Type = 'AttackEffect'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if 'LunarBloom' in AttackType:
            if self.Character.Constellation >= 6:
                AttackingCharacterStat['ElevatedMultiplier'] += 0.25

        return AttackingCharacterStat, TargetedEnemyStat

from Game import Game
from .BaseCharacter import BaseCharacter

# 버프 체크리스트
# P1 네페르 원마 (Buff)                            (complete) 
# P1 네페르 환희 곱연산 (AttackEffect)              (complete) 
# P2 네페르 공증 (Buff)                             (complete) 
# P3 파티 달개화 피증 (AttackEffect)                 (complete)     
# C1 계수증가                                        (complete)           
# C2 네페르 원마, 계수증가 (Buff, AttackEffect)      (complete) 
# C4 네페르 내성깍 (AttackEffect)                    (complete) 
# C6 환희 2타 전환 + 추가타 + 승격(AttackEffect)      (complete) 

class NeferClass(BaseCharacter):
    def __init__(self, Game : Game, Level, SkillLevel, Constellation):
        super().__init__(Game=Game,
                         Name='Nefer',
                         Weapon='Catalyst',
                         Element='Dendro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)

        if Level == 90:
            self.BaseStat['BaseHP'] += 12704
            self.BaseStat['BaseATK'] += 344
            self.BaseStat['BaseDEF'] += 799
        elif Level == 100:
            self.BaseStat['BaseHP'] += 13607
            self.BaseStat['BaseATK'] += 422
            self.BaseStat['BaseDEF'] += 856
        else:
            raise ValueError
        self.BaseStat['EM'] += 200
        self.BaseStat['CD'] += 0.384

        self.Game.Moonsign += 1

        if self.Constellation >= 3:
            self.SkillLevel['Skill'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Ult'] += 3

        self.Game.AddEffect(NeferUltAttackEffect(Game, self))
        self.Game.AddEffect(NeferP1EMBuff(Game, self))
        self.Game.AddEffect(NeferP1MultiplierAttackEffect(Game, self))
        self.Game.AddEffect(NeferP2Buff(Game, self))
        self.Game.AddEffect(NeferP3AttackEffect(Game, self))
        self.Game.AddEffect(NeferC4AttackEffect(Game, self))
        self.Game.AddEffect(NeferC6AttackEffect(Game, self))
        
        
    def NA1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Normal'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.685, 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Normal'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.809, 'DEF' : 0., 'EM' : 0}
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
    
    def SkillStart(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 1.375, 'DEF' : 0., 'EM' : 2.75}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 1.623, 'DEF' : 0., 'EM' : 3.246}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소스킬 시전',
                            AttackType = 'Basic',
                            AttackElement = 'Dendro',
                            DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCANefer1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.444, 'DEF' : 0., 'EM' : 0.887}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.524, 'DEF' : 0., 'EM' : 1.047}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (네페르) 1단',
                            AttackType = 'Basic',
                            AttackElement = 'Dendro',
                            DMGType = 'Charge',
                           Multiplier=Multiplier,
                           Print=Print)

    def SkillCANefer2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0.577, 'DEF' : 0., 'EM' : 1.153}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0.681, 'DEF' : 0., 'EM' : 1.361}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (네페르) 2단',
                            AttackType = 'Basic',
                            AttackElement = 'Dendro',
                            DMGType = 'Charge',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCANefer2C6(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 0.85}

        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (네페르) 2단 6돌',
                            AttackType = 'DirectLunarBloom',
                            AttackElement = 'Dendro',
                            DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCAShade1(self, TargetedEnemy, Reaction=None, Print=True):
        
        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.728}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.04}
        else:
            raise NotImplementedError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (환영) 1단',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCAShade2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.728}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.04}
        else:
            raise NotImplementedError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (환영) 2단',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCAShade3(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 2.304}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 0., 'DEF' : 0., 'EM' : 2.72}
        else:
            raise NotImplementedError
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 (환영) 3단',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCAFinalC6(self, TargetedEnemy, Reaction=None, Print=True):

        Multiplier = {'HP' : 0., 'ATK' : 0, 'DEF' : 0., 'EM' : 1.2}
        
        if self.Constellation >= 1:
            Multiplier['EM'] += 0.6

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 강공격 환희 6돌 추가',
                           AttackType = 'DirectLunarBloom',
                           AttackElement = 'Dendro',
                           DMGType = None,
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 4.044, 'DEF' : 0., 'EM' : 8.087}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 4.774, 'DEF' : 0., 'EM' : 9.547}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 1단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0., 'ATK' : 6.605, 'DEF' : 0., 'EM' : 12.131}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0., 'ATK' : 7.160, 'DEF' : 0., 'EM' : 14.321}
        else:
            raise NotImplementedError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 2단',
                           AttackType = 'Basic',
                           AttackElement = 'Dendro',
                           DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCACombine(self, TargetedEnemy, Print=True):
        Reaction = None
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
    
    def UltCombine(self, TargetedEnemy, Print=True):
        DMG = 0 
        DMG += self.Ult1(TargetedEnemy, None, Print=False)
        DMG += self.Ult2(TargetedEnemy, None, Print=False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG
    
    def Roatation(self, TargetedEnemy):
        DMG = 0
        DMG += self.SkillStart(TargetedEnemy, None, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)

        DMG += self.SkillStart(TargetedEnemy, None, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)
        DMG += self.SkillCACombine(TargetedEnemy, True)

        return DMG
        
    

class NeferUltAttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer Ult DMGMultiplier'
        self.Type = 'AttackEffect'

        self.Game=Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if DMGType == 'Ult':
                if self.Character.SkillLevel['Ult'] == 10:
                    Multiplier = 0.4
                elif self.Character.SkillLevel['Ult'] == 13:
                    Multiplier = 0.49
                else:
                    raise NotImplementedError

                if self.Character.Constellation >= 2:
                    stack = 5
                else:
                    stack = 3
                AttackingCharacterStat['BaseDMGMultiplier'] += Multiplier * stack
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class NeferP1EMBuff: # (범용상황, 범용버프) + (범용상황, 특정버프) + (특정상황, 특정버프) 
    def __init__(self, Game, Character):
        self.Name = 'Nefer P1 EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.Game.Moonsign >= 2:
                Stat = 'EM'
                if self.Character.Constellation >= 2:
                    Amount = 200
                else:
                    Amount = 100
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


class NeferP1MultiplierAttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer P1 CA DMGMultiplier'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
        
    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if self.Game.Moonsign >= 2:
                if '환희' in AttackName:
                    if self.Character.Constellation >= 2:
                        Multiplier = 0.5
                    else:
                        Multiplier = 0.3
                    AttackingCharacterStat['BaseDMGMultiplier'] += Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat
    
class NeferP2Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer P2 ATK Bonus'
        self.Proportional = True
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character
    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat = 'AdditiveATK'

            EM = self.Character.BuffedStat['EM']
            Amount = min(200, (EM - 500) * 0.4) if EM >= 500 else 0

            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class NeferP3AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer P3 LunarBloomDMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType == 'DirectLunarBloom':
            EM = self.Character.FinalStat['EM'] 
            Amount = min(0.14, EM * 0.000175)
            
            AttackingCharacterStat['LunarBloomBaseDMGBonus'] += Amount
        
        return AttackingCharacterStat, TargetedEnemyStat

    
class NeferC4AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer C4 Res'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if self.Character.Constellation >= 4:
            TargetedEnemyStat['DendroRes'] -= 0.2
            
        return AttackingCharacterStat, TargetedEnemyStat


class NeferC6AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nefer C6 Elevated'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackCharacter == self.Character:
            if 'LunarBloom' in AttackType:
                if self.Character.Constellation >= 6:
                    if self.Game.Moonsign >= 2:
                        AttackingCharacterStat['ElevatedMultiplier'] += 0.15

        return AttackingCharacterStat, TargetedEnemyStat

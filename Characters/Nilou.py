
from Game import Game
from .BaseCharacter import BaseCharacter

# 체크리스트
# P1 파티원마 (Buff)                (Complete)
# P2 파티개화피증 (AttackEffect)    (Complete)
# C2 적 내성깍 (Debuff)             (Complete)
# C4 닐루 궁피증 (AttackEffect)     (Complete)
# C6 닐루 치명 (Buff)               (Complete)

class NilouClass(BaseCharacter):
    def __init__(self, Game : Game, Level=90, SkillLevel = {'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation = 0, P1Active=False):
        super().__init__(Game=Game,
                         Name='Nilou',
                         Weapon='Sword',
                         Element='Hydro',
                         Level=Level,
                         SkillLevel=SkillLevel,
                         Constellation=Constellation)
 
        if Level == 90:
            self.BaseStat['BaseHP'] += 15185
            self.BaseStat['BaseATK'] += 230
            self.BaseStat['BaseDEF'] += 729
        elif Level == 100:
            self.BaseStat['BaseHP'] += 16264
            self.BaseStat['BaseATK'] += 281
            self.BaseStat['BaseDEF'] += 780
        else:
            raise ValueError
        self.BaseStat['%HP'] += 0.288

        self.P1Active= P1Active

        if self.Constellation >= 3:
            self.SkillLevel['Ult'] += 3
        
        if self.Constellation >= 5:
            self.SkillLevel['Skill'] += 3

        self.Game.AddEffect(NilouP1Buff(Game, self))
        self.Game.AddEffect(NilouP2AttackEffect(Game, self))
        self.Game.AddEffect(NilouC2Debuff(Game, self))
        self.Game.AddEffect(NilouC4Buff(Game, self))
        self.Game.AddEffect(NilouC6Buff(Game, self))
 
        
    def Skill1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0.0601, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0.0701, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 스킬 1단 (발동)',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Skill2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0.0819, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0.0967, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 스킬 2단 (검의춤)',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Skill3(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0.0926, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0.1093, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 스킬 3단 (검의춤)',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Normal',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Skill4(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Skill'] == 10:
            Multiplier = {'HP' : 0.0911, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Skill'] == 13:
            Multiplier = {'HP' : 0.1076, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 스킬 4단 (수륜)',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Skill',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult1(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0.332, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0.392, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 1단',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def Ult2(self, TargetedEnemy, Reaction=None, Print=True):

        if self.SkillLevel['Ult'] == 10:
            Multiplier = {'HP' : 0.406, 'ATK' : 0., 'DEF' : 0., 'EM' : 0.}
        elif self.SkillLevel['Ult'] == 13:
            Multiplier = {'HP' : 0.479, 'ATK' : 0., 'DEF' : 0., 'EM' : 0}
        else:
            raise ValueError

        return self.Damage(TargetedEnemy=TargetedEnemy,
                           Reaction=Reaction,
                           AttackName = f'{self.Name} 원소폭발 2단',
                            AttackType = 'Basic',
                            AttackElement = 'Hydro',
                            DMGType = 'Ult',
                           Multiplier=Multiplier,
                           Print=Print)
    
    def SkillCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.Skill1(TargetedEnemy, None, False)
        DMG += self.Skill2(TargetedEnemy, None, False)
        DMG += self.Skill3(TargetedEnemy, None, False)
        DMG += self.Skill4(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 원소스킬 총합 피해 : {DMG}')
        return DMG
    
    def UltCombine(self, TargetedEnemy, Print=True):
        DMG = 0
        DMG += self.Ult1(TargetedEnemy, None, False)
        DMG += self.Ult2(TargetedEnemy, None, False)

        if Print:
            print(f'{self.Name} 원소폭발 총합 피해 : {DMG}')
        return DMG

    def Rotation(self, TargtedEnemy):
        DMG = 0
        DMG += self.SkillCombine(TargtedEnemy, True)

        return DMG


class NilouP1Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Nilou P1 EM'
        self.Proportional = False
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if self.Character.P1Active:
            Stat = 'EM'
            Amount = 100
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class NilouP2AttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Nilou P2 BloomBuff'
        self.Type = 'AttackEffect'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType == 'Bloom':
            HP = self.Character.FinalStat['BaseHP'] * (1 + self.Character.FinalStat['%HP']) + self.Character.FinalStat['AdditiveHP']
            AttackingCharacterStat['ReactionBonus'] += min(4.0, (HP-30000)/1000 * 0.09)
        
        return AttackingCharacterStat, TargetedEnemyStat

    
class NilouC2Debuff: 
    def __init__(self, Game, Character):
        self.Name = 'Nilou C2 Res'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character
    
    def Apply(self, DebuffedEnemy, Print):
        
        if self.Character.Constellation >= 2:
            Stat1 = 'HydroRes'
            Stat2 = 'DendroRes'
            Amount = -0.35
            DebuffedEnemy.DebuffedStat[Stat1] += Amount
            DebuffedEnemy.DebuffedStat[Stat2] += Amount
            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat1:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat1]:<5.3f}")
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat2:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat2]:<5.3f}")
    
class NilouC4Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Nilou C4 UltDMGBonus'
        self.Proportional = False
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if self.Character.Constellation >= 4:
            Stat = 'UltDMGBonus'
            Amount = 0.5
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
    
class NilouC6Buff: 
    def __init__(self, Game, Character):
        self.Name = 'Nilou C6 Crit'
        self.Proportional = True
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.Character.Constellation >= 6:
                HP = self.Character.BuffedStat['BaseHP'] * (1 + self.Character.BuffedStat['%HP']) + self.Character.BuffedStat['AdditiveHP']

                Stat1 = 'CR'
                Amount1 = min(0.3, 0.006 * HP/1000)
                BuffedCharacter.FinalStat[Stat1] += Amount1
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat1:<25}: +{Amount1:<8.3f} | -> {BuffedCharacter.FinalStat[Stat1]:<5.3f}")

                Stat2 = 'CD'
                Amount2 = min(0.6, 0.012 * HP/1000)
                BuffedCharacter.FinalStat[Stat2] += Amount2
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat2:<25}: +{Amount2:<8.3f} | -> {BuffedCharacter.FinalStat[Stat2]:<5.3f}")



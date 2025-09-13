class LaumaEDebuff: 
    def __init__(self, Character=None, Constellation=0):
        self.Name = 'Lauma E Res'
        self.Proportional = False
        self.Type = 'Debuff'

        self.Character = Character
        self.Constellation = Constellation
    
    def Apply(self, DebuffedEnemy, Print):
        Stat1 = 'DendroRes'
        Stat2 = 'HydroRes'

        Constellation = self.Character.Constellation if self.Character is not None else self.Constellation

        Amount = -0.34 if Constellation >= 3 else -0.25

        DebuffedEnemy.DebuffedStat[Stat1] += Amount
        DebuffedEnemy.DebuffedStat[Stat2] += Amount
        if Print:
            print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat1:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat1]:<5.3f}")
            print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat2:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat2]:<5.3f}")



class LaumaQAttackEffect: 
    def __init__(self, Character=None, Constellation=0, EM=0, Moonsign=2):
        self.Name = 'Lauma Q DMGBonus'
        self.Proportional = True
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Constellation = Constellation
        self.EM = EM
        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        # 개화 반응 구현 X
        
        if 'LunarBloom' in AttackType:
            
            EM = self.Character.BuffedStat['EM'] if self.Character is not None else self.EM
            Constellation = self.Character.Constellation if self.Character is not None else self.Constellation

            Multiplier = 4.723 if Constellation >= 3 else 4.0
                
            if self.Constellation >= 2:
                Multiplier += 4.0
                if self.Moonsign == 2:
                    AttackingCharacterStat['ReactionBonus'] + 0.4
                
            AttackingCharacterStat['AdditiveBaseDMGBonus'] += EM * Multiplier
        
        return AttackingCharacterStat, TargetedEnemyStat
    

class LaumaP1AttackEffect: 
    def __init__(self, Character=None, Moonsign=2):
        self.Name1 = 'Lauma P1 Crit'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.Moonsign == 1:
            pass # 개화반응 구현 X

        if self.Moonsign == 2:
            if 'LunarBloom' in AttackType:
                AttackingCharacterStat['CR'] + 0.1
                AttackingCharacterStat['CD'] + 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat
    
    
class LaumaP2Buff: 
    def __init__(self, Character=None, EM=None):
        self.Name = 'Lauma P2 LunarBloomDMG'
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

    
class LaumaC6AttackEffect: 
    def __init__(self, Character=None, Constellation=6):
        self.Name = 'Lauma C6 Elevated'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Constellation = Constellation

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if 'LunarBloom' in AttackType:
            Constellation = self.Character.Constellation if self.Character is not None else self.Constellation
            if Constellation >= 6:
                AttackingCharacterStat['ElevatedMultiplier'] += 0.25

        return AttackingCharacterStat, TargetedEnemyStat

def AddLaumaTemp(Game, Constellation, EM, Moonsign):
    Game.AddEffect(LaumaEDebuff(Constellation=Constellation))
    Game.AddEffect(LaumaQAttackEffect(Constellation=Constellation, EM=EM, Moonsign=Moonsign))
    Game.AddEffect(LaumaP1AttackEffect(Moonsign=Moonsign))
    Game.AddEffect(LaumaP2Buff(EM=EM))
    Game.AddEffect(LaumaC6AttackEffect(Constellation=Constellation))

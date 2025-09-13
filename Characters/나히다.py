class NahidaP1Buff: 
    def __init__(self, Character=None, EM = 1000):
        self.Name = 'Nahida P1 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Character = Character
        self.EM = EM
    
    def Apply(self, BuffedCharacter, Print):
        Stat = 'EM'
        Amount = min(250, self.EM * 0.25)
        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class NahidaC2Debuff: 
    def __init__(self, Character=None, Constellation=2, CatalyzeActive=False):
        self.Name = 'Nahida C2 DefReduction'
        self.Proportional = False
        self.Type = 'Debuff'

        self.Character = Character
        self.Constellation = Constellation
        self.CatalyzeActive=CatalyzeActive

    def Apply(self, DebuffedEnemy, Print):
        Constellation = self.Character.Constellation if self.Character is not None else self.Constellation
        if Constellation >= 2:
            Stat = 'DEFReduction'
            Amount = 0.3
            DebuffedEnemy.DebuffedStat[Stat] += Amount
            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")

class NahidaC2AttackEffect:
    def __init__(self, Character=None, Constellation=2):
        self.Name = 'Nahida C2 Crit'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Constellation = Constellation

    def Apply(self, AttackCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        Constellation = self.Character.Constellation if self.Character is not None else self.Constellation

        if Constellation >= 2:
            # 개화 관련 반응 구현 x
            if 'LunarBloom' in AttackType:
                AttackingCharacterStat['CR'] += 0.1
                AttackingCharacterStat['CD'] += 0.2
        
        return AttackingCharacterStat, TargetedEnemyStat

def AddNahidaTemp(Game, Constellation, EM, CatalyzeActive):
    Game.AddEffect(NahidaP1Buff(EM=EM))
    Game.AddEffect(NahidaC2Debuff(Constellation=Constellation, CatalyzeActive=CatalyzeActive))
    Game.AddEffect(NahidaC2AttackEffect(Constellation=Constellation))
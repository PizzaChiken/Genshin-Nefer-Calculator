class NahidaP1Buff: 
    def __init__(self, Game, Character, EM):
        self.Name = 'Nahida P1 EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.EM = EM
    
    def Apply(self, BuffedCharacter, Print):
        Stat = 'EM'
        Amount = min(250, self.EM * 0.25)
        BuffedCharacter.FinalStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")

class NahidaC2Debuff: 
    def __init__(self, Game, Character, Constellation, CatalyzeActive):
        self.Name = 'Nahida C2 DefReduction'
        self.Type = 'Debuff'

        self.Game = Game
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
    def __init__(self, Game, Character, Constellation):
        self.Name = 'Nahida C2 Crit'
        self.Type = 'AttackEffect'

        self.Game = Game
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
    Game.AddEffect(NahidaP1Buff(Game, Character=None, EM=EM))
    Game.AddEffect(NahidaC2Debuff(Game, Character=None, Constellation=Constellation, CatalyzeActive=CatalyzeActive))
    Game.AddEffect(NahidaC2AttackEffect(Game, Character=None, Constellation=Constellation))
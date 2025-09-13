class BaseWeapon:
    def __init__(self, Character, Refinements):
        Refinements = Refinements -1
        self.StatList = {
            'BaseATK' : 542,
        }
        
        self.BuffList = []
        self.DebuffList = []
        self.AttackEffectList = []

# 파티버프
class BasicBuff: 
    def __init__(self, Character=None, Refinements=1):
        self.Name = 'Basic버프'
        self.Proportional = False
        self.Type = 'Buff'

        self.Character = Character
        self.Refinments = Refinements

    def Apply(self, BuffedCharacter, Print):
        Stat = ''
        Amount = 0
        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class BasicDebuff: 
    def __init__(self, Character=None, Refinements=1):
        self.Name = 'Basic디버프'
        self.Proportional = False
        self.Type = 'Debuff'

        self.Character = Character
        self.Refinements = Refinements

    def Apply(self, DebuffedEnemy, Print):
        Stat = ''
        Amount = 0
        DebuffedEnemy.DebuffedStat[Stat] += Amount
        if Print:
             print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")

        pass

class BasicEffect: 
    def __init__(self, Character=None, Refinements=1):
        self.Name = 'Basic공격효과'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Refinements = Refinements

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        
        return AttackingCharacterStat, TargetedEnemyStat
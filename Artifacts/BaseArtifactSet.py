class BaseArtifactSet:
    def __init__(self, Game, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'EM' : 80 
        }
        self.EffectList = []

# 파티버프
class BasicBuff: 
    def __init__(self, Game, Character=None, PC=4):
        self.Name = 'Basic버프'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.PC = PC

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

class BasicDebuff: 
    def __init__(self, Game, Character=None, PC=4):
        self.Name = 'Basic디버프'
        self.Type = 'Debuff'

        self.Game = Game
        self.Character = Character
        self.PC = PC

    def Apply(self, DebuffedEnemy, Print):
        Stat = ''
        Amount = 0
        DebuffedEnemy.DebuffedStat[Stat] += Amount
        if Print:
             print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")


class BasicAttackEffect: 
    def __init__(self, Game, Character=None, PC=4):
        self.Name = 'Basic공격효과'
        self.Type = 'AttackEffect'
        
        self.Game = Game
        self.Character = Character
        self.PC = PC

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        
        return AttackingCharacterStat, TargetedEnemyStat
class NightOfTheSkysUnveiling:
    def __init__(self, Character, PC, Moonsign = 2):
        assert PC in [2, 4]

        self.StatList = {
            'EM' : 80 
        }
        if PC == 4:
            self.EffectList = [NightOfTheSkysUnveilingPC4Buff(Character, PC), 
                               NightOfTheSkysUnveilingPC4AttackEffect(Character, PC)]

# 파티버프
class NightOfTheSkysUnveilingPC4Buff: 
    def __init__(self, Character=None, PC=4, Moonsign=2):
        self.Name = 'NightOfTheSkysUnveiling EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Character = Character
        self.PC = PC
        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.PC == 4:
                Stat = 'CR'
                Amount = 0.15 if self.Moonsign == 1 else 0.3
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class NightOfTheSkysUnveilingPC4AttackEffect: 
    def __init__(self, Character=None, PC=4, Moonsign=2):
        self.Name = 'NightOfTheSkysUnveiling ReactionBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.PC = PC
        assert Moonsign in [1,2]
        self.Moonsign = Moonsign

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if self.PC == 4:
            if 'Lunar' in AttackType:
                AttackingCharacterStat['ReactionBonus']  += 0.1
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddNightOfTheSkysUnveilingTemp(Game, PC, Moonsign):
    Game.AddEffect(NightOfTheSkysUnveilingPC4Buff(PC=PC, Moonsign=Moonsign))
    Game.AddEffect(NightOfTheSkysUnveilingPC4AttackEffect(PC=PC, Moonsign=Moonsign))
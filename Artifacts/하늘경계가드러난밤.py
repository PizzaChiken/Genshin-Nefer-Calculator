class NightOfTheSkysUnveiling:
    def __init__(self, Game, Character, PC, Moonsign):
        assert PC in [2, 4]

        self.StatList = {
            'EM' : 80 
        }
        if PC == 4:
            self.EffectList = [NightOfTheSkysUnveilingPC4Buff(Game, Character, PC, Moonsign), 
                               NightOfTheSkysUnveilingPC4AttackEffect(Game, Character, PC, Moonsign)]

# 파티버프
class NightOfTheSkysUnveilingPC4Buff: 
    def __init__(self, Game, Character, PC, Moonsign):
        self.Name = 'NightOfTheSkysUnveiling EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
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
    def __init__(self, Game, Character, PC, Moonsign):
        self.Name = 'NightOfTheSkysUnveiling ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
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
    Game.AddEffect(NightOfTheSkysUnveilingPC4Buff(Game, Character=None, PC=PC, Moonsign=Moonsign))
    Game.AddEffect(NightOfTheSkysUnveilingPC4AttackEffect(Game, Character=None, PC=PC, Moonsign=Moonsign))
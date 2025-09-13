class DeepwoodMemories:
    def __init__(self, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'DendroDMGBonus' : 0.15
        }
        if PC == 4:
            self.EffectList = [DeepwoodMemoriesDebuff(Character, PC)]

# 파티버프
class DeepwoodMemoriesDebuff: 
    def __init__(self, Character=None, PC=4):
        self.Name = 'Deepwood Memories Res'
        self.Proportional = False
        self.Type = 'Debuff'
        
        self.Character = Character
        self.PC = PC

    
    def Apply(self, DebuffedEnemy, Print):
        if self.PC == 4:
            Stat = 'DendroRes'
            Amount = -0.3
            DebuffedEnemy.DebuffedStat[Stat] += Amount

            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")

def AddDeepwoodMemorieTemp(Game, PC):
    Game.AddEffect(DeepwoodMemoriesDebuff(PC=PC))
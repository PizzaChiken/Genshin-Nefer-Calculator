# 숲의 기억

# 버프 체크리스트
# 적 내성깎 (Buff)  (complete) 

class DeepwoodMemories:
    def __init__(self, Game, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'DendroDMGBonus' : 0.15
        }
        if PC == 4:
            self.EffectList = [DeepwoodMemoriesDebuff(Game, Character, PC)]
        else:
            self.EffectList = []

# 파티버프
class DeepwoodMemoriesDebuff: 
    def __init__(self, Game, Character, PC):
        self.Name = 'Deepwood Memories Res'
        self.Type = 'Debuff'
        
        self.Game = Game
        self.Character = Character
        self.PC = PC

    
    def Apply(self, DebuffedEnemy, Print):
        if self.PC == 4:
            Stat = 'DendroRes'
            Amount = -0.3
            DebuffedEnemy.DebuffedStat[Stat] += Amount

            if Print:
                print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")
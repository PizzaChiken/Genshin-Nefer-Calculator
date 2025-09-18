# 옛 왕실의 의식
from Game import Game

#체크리스트
# 파티 공버프  (Complete)

class NoblesseOblige:
    def __init__(self, Game, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'UltDMGBonus' : 0.2 
        }

        if PC == 4:
            self.EffectList = [NoblesseObligeBuff(Game, Character, PC)]
        else:
            self.EffectList = []

class NoblesseObligeBuff: 
    def __init__(self, Game, Character, PC):
        self.Name = 'NoblesseOblige ATK'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.PC = PC


    def Apply(self, BuffedCharacter, Print):
        if self.PC == 4:
            Stat = '%ATK'
            Amount = 0.2
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")


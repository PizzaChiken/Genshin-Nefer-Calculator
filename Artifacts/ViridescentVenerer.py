# 청록색 그림자

from Game import Game

#체크리스트
# 적 디버프 (Debuff) (Complete)

class ViridescentVenerer:
    def __init__(self, Game, Character, PC, Elements):
        assert PC in [2, 4]

        self.StatList = {
            'AnemoDMGBonus' : 0.15
        }

        if PC == 4:
            self.EffectList = ViridescentVenererDebuff(Game, Character, PC, Elements), 
        else:
            self.EffectList = []


class ViridescentVenererDebuff: 
    def __init__(self, Game, Character, PC, Elements):
        self.Name = 'ViridescentVenerer Res'
        self.Type = 'Debuff'
        
        self.Game = Game
        self.Character = Character
        self.PC = PC
        self.Elements = Elements

    
    def Apply(self, DebuffedEnemy, Print):
        if self.PC == 4:
            for Element in self.Elements:
                Stat = f'{Element}Res'
                Amount = -0.4
                DebuffedEnemy.DebuffedStat[Stat] += Amount

                if Print:
                    print(f"Debuff | {self.Name :<40} | {DebuffedEnemy.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {DebuffedEnemy.DebuffedStat[Stat]:<5.3f}")
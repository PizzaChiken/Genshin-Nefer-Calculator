# 불로 벼린 지혜

# 버프 체크리스트
# 원마 (자신만 적용, 온오프) (Buff)  

class FlameForgedInsight:
    def __init__(self, Game, Character, Refinements, ReactionActive):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 510,
            'EM' : 165,
        }

        self.EffectList = [
            FlameForgedInsightBuff(Game, Character, Refinements, ReactionActive),
            ]
            

class FlameForgedInsightBuff: 
    def __init__(self, Game, Character, Refinements, ReactionActive):
        self.Name = 'FlameForgedInsight EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        
        assert Refinements in [1, 2, 3, 4, 5]

        EM = [60, 75, 90, 105, 120][Refinements-1]
        
        self.EM = EM
        self.ReactionActive = ReactionActive

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.ReactionActive:
                Stat = 'EM'
                Amount = self.EM
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

    
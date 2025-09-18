# 방랑하는 저녁별

# 버프 체크리스트
# 파티 원마 (Buff)   (Complete)          


class WanderingEvenstar:
    def __init__(self, Game, Character, Refinements):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 510,
            'EM' : 165,
        }

        self.EffectList = [
            WanderingEvenstarBuff(Game, Character, Refinements),
            ]
            

class WanderingEvenstarBuff: 
    def __init__(self, Game, Character, Refinements):
        self.Name = 'WanderingEvenstar ATK'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        
        assert Refinements in [1, 2, 3, 4, 5]

        self.EMRatio = [0.24, 0.3, 0.36, 0.42, 0.48][Refinements-1]

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat = 'AdditiveATK'
            Amount = self.Character.BuffedStat['EM'] * self.EMRatio
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")
        else:
            Stat = 'AdditiveATK'
            Amount = self.Character.BuffedStat['EM'] * self.EMRatio * 0.3
            BuffedCharacter.FinalStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.FinalStat[Stat]:<5.3f}")
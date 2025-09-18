# 오래된 자유의 서약

#체크리스트 
# 피증, 공퍼 (Complete)

class FreedomSworn:
    def __init__(self, Game, Character, Refinements, Active, NoATKBuff):
        assert Refinements in [1, 2, 3, 4, 5]
        self.StatList = {
            'BaseATK' : 608,
            'EM' : 198,
            'DMGBonus' : [0.1, 0.125, 0.15, 0.175, 0.2][Refinements-1],
        }
        self.EffectList = [FreedomSwornBuff(Game, Character, Refinements, Active, NoATKBuff)]

# 파티버프
class FreedomSwornBuff: 
    def __init__(self, Game, Character, Refinements, Active, NoATKBuff):
        self.Name = 'FreedomSworn Buff'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]
        self.DMGBonus = [0.16, 0.2, 0.24, 0.28, 0.32][Refinements-1]
        self.ATK = [0.2, 0.25, 0.3, 0.35, 0.4][Refinements-1]

        self.Active = Active
        self.NoATKBuff = NoATKBuff
    
    def Apply(self, BuffedCharacter, Print):
        if self.Active:
            Stat1 = 'NormalDMGBonus'
            Amount = self.DMGBonus
            BuffedCharacter.BuffedStat[Stat1] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat1:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat1]:<5.3f}")
        
            Stat2 = 'ChargeDMGBonus'
            BuffedCharacter.BuffedStat[Stat2] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat2:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat2]:<5.3f}")

            Stat3 = 'PlungingDMGBonus'
            BuffedCharacter.BuffedStat[Stat3] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat3:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat3]:<5.3f}")

            if not self.NoATKBuff:
                Stat4 = '%ATK'
                Amount4 = self.ATK
                BuffedCharacter.BuffedStat[Stat4] += Amount4
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat4:<25}: +{Amount4:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat4]:<5.3f}")
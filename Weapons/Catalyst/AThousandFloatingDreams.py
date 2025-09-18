# 떠오르는 천일 밤의 꿈

# 버프 체크리스트
# 캐릭터 원미/피증 (Buff)  (complete) 
# 파티 원마 (Buff)          (complete) 

class AThousandFloatingDreams:
    def __init__(self, Game, Character, Refinements, Cnt): # Cnt : [원소동일개수, 비동일개수])
        assert Refinements in [1, 2, 3, 4, 5]
        assert Cnt[0] + Cnt[1] == 3
    
        self.StatList = {
            'BaseATK' : 542,
            'EM' : 265
        }
        self.EffectList = [AThousandFloatingDreamsBuff(Game, Character, Refinements, Cnt)]

# 파티버프
class AThousandFloatingDreamsBuff: 
    def __init__(self, Game, Character, Refinements, Cnt):
        self.Name = 'AThousandFloatingDreams Buffs'
        self.Proportional = False
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]

        self.EMSelf = [32, 40, 48, 56, 64][Refinements-1] * Cnt[0]
        self.DMGBonusSelf = [0.1, 0.14, 0.18, 0.22, 0.26][Refinements-1] * Cnt[1]
        self.EMParty = [40, 42, 44, 46, 48][Refinements-1]
    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat1 = 'EM'
            Amount1 = self.EMSelf
            BuffedCharacter.BuffedStat[Stat1] += Amount1
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat1:<25}: +{Amount1:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat1]:<5.3f}")

            Stat2 = 'DMGBonus'
            Amount2 = self.DMGBonusSelf
            BuffedCharacter.BuffedStat[Stat2] += Amount2
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat2:<25}: +{Amount2:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat2]:<5.3f}")

        Stat3 = 'EM'
        Amount3 = self.EMParty
        BuffedCharacter.BuffedStat[Stat3] += Amount3
        if Print:
            print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat3:<25}: +{Amount3:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat3]:<5.3f}")

    
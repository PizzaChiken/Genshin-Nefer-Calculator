class NahidaSignature:
    def __init__(self, Game, Character, Refinements, Cnt): # Cnt : [원소동일개수, 비동일개수])
        assert Refinements in [1, 2, 3, 4, 5]
        assert Cnt[0] + Cnt[1] == 3
    
        self.StatList = {
            'BaseATK' : 542,
            'EM' : 265 + [32, 40, 48, 56, 64][Refinements-1] * Cnt[0],
            'DMGBonus' : [0.10, 0.14, 0.18, 0.26][Refinements-1] * Cnt[1],
        }
        self.EffectList = [NahidaSignatureBuff(Game, Character, Refinements, Cnt)]

# 파티버프
class NahidaSignatureBuff: 
    def __init__(self, Game, Character, Refinements):
        self.Name = 'Nahida Signature Buffs'
        self.Proportional = False
        self.Type = 'Buff'
        
        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]
    
        self.EMParty = [40, 42, 44, 46, 48][Refinements-1]
    
    def Apply(self, BuffedCharacter, Print):

        Stat3 = 'EM'
        Amount3 = self.EMParty
        BuffedCharacter.BuffedStat[Stat3] += Amount3
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat3:<25}: +{Amount3:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat3]:<5.3f}")

def AddNahidaSignatureTemp(Game, Refinements):
    Game.AddEffect(NahidaSignatureBuff(Game=Game, Character=None, Refinements=Refinements))

    
class NahidaSignature:
    def __init__(self, Character, Refinements, Cnt = [2, 1]): # [원소동일개수, 비동일개수])
        Refinements = Refinements -1
        EM = [32, 40, 48, 56, 64]
        DMGBonus = [0.10, 0.14, 0.18, 0.26]
        self.StatList = {
            'BaseATK' : 542,
            'EM' : EM[Refinements] * Cnt[0],
            'DMGBonus' : DMGBonus[Refinements] * Cnt[1]
        }
        self.EffectList = [NahidaSignatureBuff(Character, Refinements)]

# 파티버프
class NahidaSignatureBuff: 
    def __init__(self, Character=None, Refinements=1):
        self.Name = 'Nahida Signature EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Character = Character
        self.Refinements = Refinements

        self.EM = [40, 42, 44, 46, 48]
    
    def Apply(self, BuffedCharacter, Print):
        Stat = 'EM'
        Amount = self.EM[self.Refinements]
        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

def AddNahidaSignatureTemp(Game, Refinements):
    Refinements = Refinements - 1
    Game.AddEffect(NahidaSignatureBuff(Refinements=Refinements))

    
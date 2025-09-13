class NilouSignature:
    def __init__(self, Character, Refinements):
        Refinements = Refinements -1
        HP = [0.2, 0.25, 0.3, 0.35, 0.4]
        self.StatList = {
            'BaseATK' : 542,
            '%HP' : 0.662 + HP[Refinements],
        }
        self.EffectList = [NilouSignatureBuff(Character, Refinements)]

# 파티버프
class NilouSignatureBuff: 
    def __init__(self, Character=None, Refinements=1, HP=74444):
        self.Name = 'Nilou Signature EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Character = Character
        self.Refinements = Refinements

        self.HP = HP

        assert (Character != None) or (HP != None)

        self.Multiplier1 = [0.0012, 0.0015, 0.0018, 0.0021, 0.0024]
        self.Multiplier2 = [0.0020, 0.0025, 0.0030, 0.0035, 0.0040]

    
    def Apply(self, BuffedCharacter, Print):
        HP = self.Character.BuffedStat['HP'] if self.Character is not None else self.HP
        Stat = 'EM'
        Amount = HP * self.Multiplier1[self.Refinements] * 3 + HP * self.Multiplier2[self.Refinements]
        
        BuffedCharacter.BuffedStat[Stat] += Amount
        if Print:
             print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

def AddNilouSignatureTemp(Game, Refinements, HP):
    Refinements = Refinements - 1
    Game.AddEffect(NilouSignatureBuff(Refinements=Refinements, HP=HP))

    
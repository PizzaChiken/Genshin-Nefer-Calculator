class NilouSignature:
    def __init__(self, Game, Character, Refinements):
        assert Refinements in [1, 2, 3, 4, 5]
        self.StatList = {
            'BaseATK' : 542,
            '%HP' : 0.662 + [0.2, 0.25, 0.3, 0.35, 0.4][Refinements-1],
        }
        self.EffectList = [NilouSignatureBuff(Game, Character, Refinements)]

# 파티버프
class NilouSignatureBuff: 
    def __init__(self, Game, Character, Refinements, HP):
        self.Name = 'Nilou Signature EM'
        self.Proportional = True
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.HP = HP

        assert Refinements in [1, 2, 3, 4, 5]
        self.Multiplier1 = [0.0012, 0.0015, 0.0018, 0.0021, 0.0024][Refinements-1]
        self.Multiplier2 = [0.0020, 0.0025, 0.0030, 0.0035, 0.0040][Refinements-1]

    
    def Apply(self, BuffedCharacter, Print):
        HP = self.Character.BuffedStat['HP'] if self.Character is not None else self.HP

        if BuffedCharacter == self.Character:
            Stat1 = 'EM'
            Amount1 = HP * self.Multiplier1 * 3
            
            BuffedCharacter.FinalStat[Stat1] += Amount1
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat1:<25}: +{Amount1:<8.3f} | -> {BuffedCharacter.FinalStat[Stat1]:<5.3f}")
        
        Stat2 = 'EM'
        Amount2 = HP * self.Multiplier2
        
        BuffedCharacter.FinalStat[Stat2] += Amount2
        if Print:
            print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat2:<25}: +{Amount2:<8.3f} | -> {BuffedCharacter.FinalStat[Stat2]:<5.3f}")

def AddNilouSignatureTemp(Game, Refinements, HP):
    Game.AddEffect(NilouSignatureBuff(Game, Character=None, Refinements=Refinements, HP=HP))

    
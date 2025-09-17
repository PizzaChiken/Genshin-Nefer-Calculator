# 버프 체크리스트
# 캐릭터 원미/치피 (Buff)  (complete) 

class ReliquaryofTruth: # 네페르전무
    def __init__(self, Game, Character, Refinements, LunarBloomActive, SkillActive):
        assert Refinements in [1, 2, 3, 4, 5]
        self.StatList = {
            'BaseATK' : 542,
            'CD' : 0.882,
            'CR' : [0.08, 0.10, 0.12, 0.14, 0.16][Refinements-1]
        }
        self.EffectList = [ReliquaryofTruthBuff(Game, Character, Refinements, LunarBloomActive, SkillActive)]

class ReliquaryofTruthBuff: 
    def __init__(self, Game, Character, Refinements, LunarBloomActive, SkillActive):
        self.Name = 'ReliquaryofTruth Buffs'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]
    
        self.EMSelf = [80, 100, 120, 140, 160][Refinements-1] if SkillActive else 0
        self.CDSelf = [0.24, 0.30, 0.36, 0.42, 0.48][Refinements-1] if LunarBloomActive else 0

        if LunarBloomActive and SkillActive:
            self.EMSelf = self.EMSelf * 1.5
            self.CDSelf = self.CDSelf * 1.5

    
    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat1 = 'EM'
            Amount1 = self.EMSelf
            BuffedCharacter.BuffedStat[Stat1] += Amount1
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat1:<25}: +{Amount1:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat1]:<5.3f}")
            
            Stat2 = 'CD'
            Amount2 = self.CDSelf
            BuffedCharacter.BuffedStat[Stat2] += Amount2
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat2:<25}: +{Amount2:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat2]:<5.3f}")
class LaumaSignature:
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 542,
            'EM' : 265,
        }

        self.EffectList = [
            LaumaSignatureBuff(Game, Character, Refinements, SkillActive, LunarBloomActive),
            LaumaSignatureAttackEffect(Game, Character, Refinements, SkillActive, LunarBloomActive)
            ]
            

class LaumaSignatureBuff: 
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        self.Name = 'LaumaSignatureEM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        
        assert Refinements in [1, 2, 3, 4, 5]

        EM = [60, 75, 90, 105, 120][Refinements-1]
        
        self.EMBonus = EM if SkillActive else 0
        self.EMBonus2 = EM if LunarBloomActive else 0


    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            Stat = 'EM'
            Amount = self.EMBonus + self.EMBonus2
            BuffedCharacter.BuffedStat[Stat] += Amount
            if Print:
                print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            
class LaumaSignatureAttackEffect: 
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        self.Name = 'Lauma Signature LunarBloomDMGBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]
        self.ReactionBonus = [0.4, 0.5, 0.6, 0.7, 0.8][Refinements-1]
        self.BothActive = SkillActive and LunarBloomActive

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        # 개화관련 NotImplemented
        if 'LunarBloom' in AttackType:
            if self.BothActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddLaumaSignatureTemp(Game, Refinements, SkillActive, LunarBloomActive):
    Game.AddEffect(LaumaSignatureAttackEffect(Game, Character=None, Refinements=Refinements, SkillActive=SkillActive, LunarBloomActive=LunarBloomActive))
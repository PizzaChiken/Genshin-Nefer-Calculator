class LaumaSignature:
    def __init__(self, Character, Refinements, SkillActive=True, LunarBloomActive=True):
        Refinements = Refinements -1
        EM = [60, 75, 90, 105, 120]
        
        EMBonus = EM[Refinements] if SkillActive else 0
        EMBonus2 = EM[Refinements] if LunarBloomActive else 0

        self.StatList = {
            'BaseATK' : 542,
            'EM' : 265 + EMBonus + EMBonus2,
        }

        self.EffectList = [LaumaSignatureAttackEffect(Character, Refinements, SkillActive, LunarBloomActive)]

# 파티버프
class LaumaSignatureAttackEffect: 
    def __init__(self, Character=None, Refinements=1, SkillActive=True, LunarBloomActive=True):
        self.Name = 'Lauma Signature LunarBloomDMGBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.ReactionBonus = [0.4, 0.5, 0.6, 0.7, 0.8][Refinements]

        self.BothActive = SkillActive and LunarBloomActive

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        # 개화관련 NotImplemented
        if 'LunarBloom' in AttackType:
            if self.BothActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddLaumaSignatureTemp(Game, Refinements):
    Refinements = Refinements - 1
    Game.AddEffect(LaumaSignatureAttackEffect(Refinements=Refinements))
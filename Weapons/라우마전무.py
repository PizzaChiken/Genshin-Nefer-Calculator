class LaumaSignature:
    def __init__(self, Character, Refinements):
        Refinements = Refinements -1
        EM1 = [60, 75, 90, 105, 120]
        self.StatList = {
            'BaseATK' : 542,
            'EM' : EM1[Refinements] * 2
        }
        self.EffectList = [LaumaSignatureAttackEffect(Character, Refinements)]

# 파티버프
class LaumaSignatureAttackEffect: 
    def __init__(self, Character=None, Refinements=1):
        self.Name = 'Lauma Signature LunarBloomDMGBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.Character = Character
        self.Refinements = Refinements
        self.ReactionBonus = [0.4, 0.5, 0.6, 0.7, 0.8]

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        # 개화관련 반응 구현 X
        if 'LunarBloom' in AttackType:
            AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus[self.Refinements]
        
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddLaumaSignatureTemp(Game, Refinements):
    Refinements = Refinements - 1
    Game.AddEffect(LaumaSignatureAttackEffect(Refinements=Refinements))
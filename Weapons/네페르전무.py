class NeferSignature: # 네페르전무
    def __init__(self, Character, Refinements, LunarBloomActive, SkillActive=True):
        Refinements = Refinements -1
        CR = [0.08, 0.10, 0.12, 0.14, 0.16]
        EM = [80, 100, 120, 140, 160]
        CD = [0.24, 0.30, 0.36, 0.42, 0.48]


        CRBonus = CR[Refinements]
        EMBonus = EM[Refinements] if SkillActive else 0
        CDBonus = CD[Refinements] if LunarBloomActive else 0

        if LunarBloomActive and SkillActive:
            EMBonus = EMBonus * 1.5
            CDBonus = CDBonus * 1.5

        self.StatList = {
            'BaseATK' : 542,
            'CD' : 0.882 + CDBonus,
            'CR' : CRBonus,
            'EM' : EMBonus,
        }
        self.EffectList = []
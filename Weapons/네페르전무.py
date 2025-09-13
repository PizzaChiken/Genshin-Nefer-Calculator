class NeferSignature: # 네페르전무
    def __init__(self, Character, Refinements, LunarBloomActive=True):
        Refinements = Refinements -1
        CR = [0.08, 0.10, 0.12, 0.14, 0.16]
        EM = [80, 100, 120, 140, 160]
        CD = [0.24, 0.30, 0.36, 0.42, 0.48]

        self.StatList = {
            'BaseATK' : 542,
            'CD' : 0.882,
            'CR' : CR[Refinements],
            'EM' : EM[Refinements] * 1.5 if LunarBloomActive else EM[Refinements],
            'CD' : CD[Refinements] * 1.5 if LunarBloomActive else CD[Refinements]
        }
        self.EffectList = []
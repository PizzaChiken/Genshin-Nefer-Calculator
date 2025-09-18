#  매의 검

#체크리스트 
# 피증, 공퍼 (Complete)

class AquilaFavonia:
    def __init__(self, Game, Character, Refinements):
        assert Refinements in [1, 2, 3, 4, 5]
        self.StatList = {
            'BaseATK' : 674,
            'PhysicalDMGBonus' : 0.413,
            '%ATK' : [0.2, 0.25, 0.3, 0.35, 0.4][Refinements-1],
        }
        self.EffectList = []
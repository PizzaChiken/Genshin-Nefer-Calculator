# 피로 물든 성

# 버프 체크리스트
# 치피버프 (자신만 적용, 온오프) (Buff)             (complete)
# 달감전 피증(자신만 적용, 온오프) (AttackEffect)   (complete)

class BloodsoakedRuins:
    def __init__(self, Game, Character, Refinements, UltActive, LunarChargedActive):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 674,
            'CR' : 0.221,
        }

        self.EffectList = [
            BloodsoakedRuinsBuff(Game, Character, Refinements, LunarChargedActive),
            BloodsoakedRuinsAttackEffect(Game, Character, Refinements, UltActive)
            ]
            

class BloodsoakedRuinsBuff: 
    def __init__(self, Game, Character, Refinements, LunarChargedActive):
        self.Name = 'BloodsoakedRuins CD'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        
        assert Refinements in [1, 2, 3, 4, 5]

        CD = [0.28, 0.35, 0.42, 0.49, 0.56][Refinements-1]
        
        self.CD = CD
        self.LunarChargedActive = LunarChargedActive

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.LunarChargedActive:
                Stat = 'CD'
                Amount = self.CD
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            
class BloodsoakedRuinsAttackEffect: 
    def __init__(self, Game, Character, Refinements, UltActive):
        self.Name = 'BloodsoakedRuins ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

        self.UltActive = UltActive

        assert Refinements in [1, 2, 3, 4, 5]
        self.ReactionBonus = [0.36, 0.48, 0.6, 0.72, 0.84][Refinements-1]


    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackingCharacter == self.Character:
            if AttackType in ['DirectLunarCharged', 'LunarCharged']:
                if self.UltActive:
                    AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus
            
        return AttackingCharacterStat, TargetedEnemyStat
    
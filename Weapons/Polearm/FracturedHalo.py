# 파멸의 빛고리

# 버프 체크리스트
# 공버프 (자신만 들어가는지, 온오프) (Buff)             (complete)
# 달감전 피증(파티 전체 적용, 온오프) (AttackEffect)    (complete)

class FracturedHalo:
    def __init__(self, Game, Character, Refinements, SkillActive, ShieldActive):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 608,
            'CD' : 0.662,
        }

        self.EffectList = [
            FracturedHaloBuff(Game, Character, Refinements, SkillActive),
            FracturedHaloAttackEffect(Game, Character, Refinements, ShieldActive)
            ]
            

class FracturedHaloBuff: 
    def __init__(self, Game, Character, Refinements, SkillActive):
        self.Name = 'FracturedHalo %ATK'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        
        assert Refinements in [1, 2, 3, 4, 5]

        ATK = [0.24, 0.3, 0.36, 0.42, 0.48][Refinements-1]
        
        self.ATK = ATK
        self.Active = SkillActive

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.Active:
                Stat = '%ATK'
                Amount = self.ATK
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            
class FracturedHaloAttackEffect: 
    def __init__(self, Game, Character, Refinements, ShieldActive):
        self.Name = 'FracturedHalo LunaCharged DMG'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

        self.ShieldActive = ShieldActive

        assert Refinements in [1, 2, 3, 4, 5]
        self.ReactionBonus = [0.4, 0.5, 0.6, 0.7, 0.8][Refinements-1]


    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):

        if AttackType in ['DirectLunarCharged', 'LunarCharged']:
            if self.ShieldActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus
        
        return AttackingCharacterStat, TargetedEnemyStat
    
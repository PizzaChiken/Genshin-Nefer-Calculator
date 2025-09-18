# 밤을 엮는 거울

# 버프 체크리스트
# 캐릭터 원미 (Buff)                         (complete) 
# 파티 개화 피증, 달개화 피증 (AttackEffect)   (complete) 


class NightweaversLookingGlass:
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        assert Refinements in [1, 2, 3, 4, 5]
        
        self.StatList = {
            'BaseATK' : 542,
            'EM' : 265,
        }

        self.EffectList = [
            NightweaversLookingGlassBuff(Game, Character, Refinements, SkillActive, LunarBloomActive),
            NightweaversLookingGlassAttackEffect(Game, Character, Refinements, SkillActive, LunarBloomActive)
            ]
            

class NightweaversLookingGlassBuff: 
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        self.Name = 'NightweaversLookingGlassEM'
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
            
class NightweaversLookingGlassAttackEffect: 
    def __init__(self, Game, Character, Refinements, SkillActive, LunarBloomActive):
        self.Name = 'NightweaversLookingGlass LunarBloomDMGBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character

        assert Refinements in [1, 2, 3, 4, 5]
        self.ReactionBonus1 = [1.2, 1.5, 1.8, 2.1, 2.4][Refinements-1]
        self.ReactionBonus2 = [0.8, 1.0, 1.2, 1.4, 1.6][Refinements-1]
        self.ReactionBonus3 = [0.4, 0.5, 0.6, 0.7, 0.8][Refinements-1]
        self.BothActive = SkillActive and LunarBloomActive

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if AttackType == 'Bloom':
            if self.BothActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus1
        
        elif AttackType in ['Burgeon', 'Hyperbloom']:
            if self.BothActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus2
        
        elif AttackType == 'DirectLunarBloom':
            if self.BothActive:
                AttackingCharacterStat['ReactionBonus'] += self.ReactionBonus3
        
        return AttackingCharacterStat, TargetedEnemyStat
    
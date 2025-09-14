class NotNordAttackEffect: 
    def __init__(self, Game, ReactionBonus):
        self.Name = 'Not Nord LunarDMGBonus'
        self.Type = 'AttackEffect'

        self.Game =Game
        self.ReactionBonus = ReactionBonus

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if 'Lunar' in AttackType:
                AttackingCharacterStat['ReactionBonus']  += self.ReactionBonus
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddNotNordTemp(Game, ReactionBonus):
    Game.AddEffect(NotNordAttackEffect(Game, ReactionBonus))
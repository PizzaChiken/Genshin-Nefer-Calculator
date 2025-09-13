class NotNordAttackEffect: 
    def __init__(self, ReactionBonus):
        self.Name = 'Not Nord LunarDMGBonus'
        self.Proportional = False
        self.Type = 'AttackEffect'

        self.ReactionBonus = ReactionBonus

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if 'Lunar' in AttackType:
                AttackingCharacterStat['ReactionBonus']  += self.ReactionBonus
        return AttackingCharacterStat, TargetedEnemyStat
    
def AddNotNordTemp(Game, ReactionBonus):
    Game.AddEffect(NotNordAttackEffect(ReactionBonus))
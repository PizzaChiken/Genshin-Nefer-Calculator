# 하늘 경계가 드러난 밤

# 체크리스트
# 캐릭터 치확(Buff)  (complete) 
# 파티 달반응 피해 (AttackEffect)  (complete) 
class NightOfTheSkysUnveiling:
    def __init__(self, Game, Character, PC):
        assert PC in [2, 4]

        self.StatList = {
            'EM' : 80 
        }
        if PC == 4:
            self.EffectList = [NightOfTheSkysUnveilingPC4Buff(Game, Character, PC), 
                               NightOfTheSkysUnveilingPC4AttackEffect(Game, Character, PC)]
        else:
            self.EffectList = []

# 파티버프
class NightOfTheSkysUnveilingPC4Buff: 
    def __init__(self, Game, Character, PC):
        self.Name = 'NightOfTheSkysUnveiling EM'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.Character = Character
        self.PC = PC

    def Apply(self, BuffedCharacter, Print):
        if BuffedCharacter == self.Character:
            if self.PC == 4:
                Stat = 'CR'
                Amount = min(2, self.Game.Moonsign) * 0.15
                BuffedCharacter.BuffedStat[Stat] += Amount
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")

class NightOfTheSkysUnveilingPC4AttackEffect: 
    def __init__(self, Game, Character, PC):
        self.Name = 'NightOfTheSkysUnveiling ReactionBonus'
        self.Type = 'AttackEffect'

        self.Game = Game
        self.Character = Character
        self.PC = PC

    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, DMGType):
        if self.PC == 4:
            if AttackType in ['DirectLunarCharged', 'LunarCharged', 'DirectLunarBloom']:
                AttackingCharacterStat['ReactionBonus']  += 0.1
        
        return AttackingCharacterStat, TargetedEnemyStat
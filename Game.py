import random
import copy
import pprint


class Game:
    def __init__(self):
        self.Characters = []
        self.Enemys = []

        self.BuffList = []
        self.ProportionalBuffList = []
        self.DebuffList = []
        self.ProportionalDebuffList = []
        self.AttackEffectList = []
        self.ProportionalAttackEffectList = []

        self.PrintAll = False
    
    def initCalc(self):
        self.ApplyBuffs()
        self.ApplyDebuffs()

    def AddCharacter(self, Character):
        self.Characters.append(Character)
    
    def AddEnemy(self, Enemy):
        self.Enemys.append(Enemy)

    def AddEffect(self, Effect):
        if Effect.Type == 'Buff':
            if not Effect.Proportional:
                self.BuffList.append(Effect)
            else:
                self.ProportionalBuffList.append(Effect)

        elif Effect.Type == 'Debuff':
            if not Effect.Proportional:
                self.DebuffList.append(Effect)
            else:
                self.ProportionalDebuffList.append(Effect)

        elif Effect.Type == 'AttackEffect':
            if not Effect.Proportional:
                self.AttackEffectList.append(Effect)
            else:
                self.ProportionalAttackEffectList.append(Effect)
        else:
            raise ValueError
    
    def ApplyBuffs(self):
        for Character in self.Characters:
            Character.initBuffedStat()
        for Character in self.Characters:
            for Buff in self.BuffList:
                Buff.Apply(Character, Print=self.PrintAll)
        for Character in self.Characters:
            for Buff in self.ProportionalBuffList:
                Buff.Apply(Character, Print=self.PrintAll)
    
    def ApplyDebuffs(self):
        for Enemy in self.Enemys:
            Enemy.initDebuffedStat()
        for Enemy in self.Enemys:
            for Debuff in self.DebuffList:
                Debuff.Apply(Enemy, Print=self.PrintAll)
        for Enemy in self.Enemys:
            for Debuff in self.ProportionalDebuffList:
                Debuff.Apply(Enemy, Print=self.PrintAll)

    def ApplyAttackEffect(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        """
        AttackElement : 공격 원소 타입 : ['Physical', 'Pyro', 'Hydro', 'Electro', 'Anemo', 'Cryo', 'Geo', 'Dendro']
        Reaction : 공격 원소 반응 : ['촉진', '발산', '융해', '증발']
        AttackType : 공격 방식 : ['Basic', 'DirectLunarCharged', 'DirectLunarBloom']
        SkillType : 어떤 스킬인지 [Normal, Charge, Plunging, Skill, Ult]
        DMGType : 어떤 스킬피해인지 [Normal, Charge, Plunging, Skill, Ult]
        ]
        """
        assert AttackElement in ['Physical', 'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cyro']
        assert Reaction in [None, '촉진', '발산', '융해', '증발']
        assert AttackType in ['Basic', 'DirectLunarCharged', 'DirectLunarBloom']
        assert SkillType in [None, 'Normal', 'Charge', 'Plunging', 'Skill', 'Ult']
        assert DMGType in [None, 'Normal', 'Charge', 'Plunging', 'Skill', 'Ult']
        if AttackType in ['DirectLunarCharged', 'DirectLunarBloom']:
            assert DMGType == Reaction == None

        for AttackEffect in self.AttackEffectList:
            AttackingCharacterStatNew, TargetedEnemyStatNew = AttackEffect.Apply(AttackingCharacter, TargetedEnemy, AttackingCharacterStat.copy(), TargetedEnemyStat.copy(), AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)
            
            if self.PrintAll:
                for Stat in AttackingCharacterStat.keys():
                    if AttackingCharacterStat[Stat] != AttackingCharacterStatNew[Stat]:
                         print(f"Effect | {AttackEffect.Name:<40} | {Stat:<25}: {AttackingCharacterStat[Stat]:<5.3f} -> {AttackingCharacterStatNew[Stat]:<5.3f}")
                for Stat in TargetedEnemyStat.keys():
                    if TargetedEnemyStat[Stat] != TargetedEnemyStatNew[Stat]:
                         print(f"Effect |{AttackEffect.Name :<40} | {Stat:<25}: {TargetedEnemyStat[Stat]:<5.3f} -> {TargetedEnemyStatNew[Stat]:<5.3f}")

            AttackingCharacterStat, TargetedEnemyStat = AttackingCharacterStatNew, TargetedEnemyStatNew

        for AttackEffect in self.ProportionalAttackEffectList:
            AttackingCharacterStatNew, TargetedEnemyStatNew = AttackEffect.Apply(AttackingCharacter, TargetedEnemy, AttackingCharacterStat.copy(), TargetedEnemyStat.copy(), AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)

            if self.PrintAll:
                for Stat in AttackingCharacterStat.keys():
                    if AttackingCharacterStat[Stat] != AttackingCharacterStatNew[Stat]:
                        print(f"Effect | {AttackEffect.Name:<40} | {Stat:<25}: {AttackingCharacterStat[Stat]:<5.3f} -> {AttackingCharacterStatNew[Stat]:<5.3f}")
                for Stat in TargetedEnemyStat.keys():
                    if TargetedEnemyStat[Stat] != TargetedEnemyStatNew[Stat]:
                        print(f"Effect | {AttackEffect.Name:<40} | {Stat:<25}: {TargetedEnemyStat[Stat]:<5.3f} -> {TargetedEnemyStatNew[Stat]:<5.3f}")

            AttackingCharacterStat, TargetedEnemyStat = AttackingCharacterStatNew, TargetedEnemyStatNew

        return AttackingCharacterStat, TargetedEnemyStat
        

    def ApplyDMG(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        '''
        목표 객체에게 가하는 데미지(격변 제외)를 계산하고 적용하는 함수
        '''
        assert AttackElement in ['Physical', 'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cyro']
        assert Reaction in [None, '촉진', '발산', '융해', '증발']
        assert AttackType in ['Basic', 'DirectLunarCharged', 'DirectLunarBloom']
        if AttackType in ['DirectLunarCharged', 'DirectLunarBloom']: 
            assert Reaction == None

        HP = AttackingCharacterStat['BaseHP'] * (1 + AttackingCharacterStat['%HP']) + AttackingCharacterStat['AdditiveHP']
        ATK = AttackingCharacterStat['BaseATK'] * (1 + AttackingCharacterStat['%ATK']) + AttackingCharacterStat['AdditiveATK']
        DEF = AttackingCharacterStat['BaseDEF'] * (1 + AttackingCharacterStat['%DEF']) + AttackingCharacterStat['AdditiveDEF']
        EM = AttackingCharacterStat['EM'] 

        if self.PrintAll:
            print(f'Stats      | HP : {HP:<5} | ATK : {ATK:<5} | DEF : {DEF:<5}')
            print(f'AttackType | {AttackType}')
            print(f'Multiplier | {Multiplier}')
            print(f'CharStat   | {AttackingCharacterStat}')
            print(f'EnemyStat  | {TargetedEnemyStat}')
        
        if AttackType == 'Basic':
            BaseDMG = HP * Multiplier['HP'] + ATK * Multiplier['ATK'] + DEF * Multiplier['DEF'] + EM * Multiplier['EM']

            BaseDMG = BaseDMG * (1 + AttackingCharacterStat['BaseDMGMultiplier'])

            BaseDMG = BaseDMG + AttackingCharacterStat['AdditiveBaseDMGBonus']

            if Reaction in ['촉진', '발산']:
                if Reaction == '촉진':
                    ReactionMultiplier = 1.15
                elif Reaction == '발산':
                    ReactionMultiplier = 1.25
                else:
                    raise ValueError

                if AttackingCharacterStat['Level'] == 90:
                    LevelMultiplier = 1446.8535
                elif AttackingCharacterStat['Level'] == 95:
                    LevelMultiplier = 1561.468
                elif AttackingCharacterStat['Level'] == 100:
                    LevelMultiplier = 1674.8092
                else:
                    raise ValueError

                EMBonus = (5 * EM) / (EM + 1200)

                BaseDMG = BaseDMG + ReactionMultiplier * LevelMultiplier * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])
        
            DMGBonusMultiplier = (1 + +AttackingCharacterStat[f'{AttackElement}DMGBonus'] + AttackingCharacterStat['DMGBonus'] - TargetedEnemyStat['DMGReduction'])

            k = (1 - AttackingCharacterStat['DEFIgnored']) * (1 - TargetedEnemyStat['DEFReduction'])

            DEFMultiplier = (AttackingCharacterStat['Level'] + 100) / (k * (AttackingCharacterStat['Level'] + 100) + (AttackingCharacterStat['Level'] + 100))
            
            if Reaction in ['융해', '증발']:
                if Reaction == '융해':
                    if AttackElement == 'Pyro':
                        ReactionMultiplier = 2.0
                    elif AttackElement == 'Cyro':
                        ReactionMultiplier = 1.5
                    else:
                        raise ValueError
                elif Reaction == '증발':
                    if AttackElement == 'Hydro':
                        ReactionMultiplier = 2.0
                    elif AttackElement == 'Pyro':
                        ReactionMultiplier = 1.5
                    else:
                        raise ValueError
                
                EMBonus = 2.78 * EM / (EM + 1400)

                AmplifyingMultiplier = ReactionMultiplier * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])
            else:
                AmplifyingMultiplier = 1.

            DMG = BaseDMG * DMGBonusMultiplier * DEFMultiplier * AmplifyingMultiplier

        elif AttackType == 'DirectLunarCharged':
            BaseDMG = HP * Multiplier['HP'] + ATK * Multiplier['ATK'] + DEF * Multiplier['DEF'] + EM * Multiplier['EM']
            
            BaseDMG = BaseDMG * (1 + AttackingCharacterStat['LunarChargedBaseDMGBonus'])

           

            EMBonus = (6 * EM) / (EM + 2000)

            BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

            DMG = BaseDMG * 3

            DMG = DMG * AttackingCharacterStat['ElevatedMultiplier']
        
        elif AttackType == 'DirectLunarBloom':
            BaseDMG = HP * Multiplier['HP'] + ATK * Multiplier['ATK'] + DEF * Multiplier['DEF'] + EM * Multiplier['EM']

            BaseDMG = BaseDMG * (1 + AttackingCharacterStat['LunarBloomBaseDMGBonus'])

            BaseDMG = BaseDMG * (1 + AttackingCharacterStat['BaseDMGMultiplier'])

            EMBonus = (6 * EM) / (EM + 2000)

            BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

            DMG = BaseDMG + AttackingCharacterStat['AdditiveBaseDMGBonus']

            DMG = DMG * AttackingCharacterStat['ElevatedMultiplier']
        
        else:
            raise ValueError        
                        
        Res = TargetedEnemyStat[f'{AttackElement}Res']
        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)

        if AttackingCharacterStat['CR'] > 1.0:
            print(f'오버 치확 발생, 현재 치확: {AttackingCharacterStat["CR"]}')

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['CR']) * AttackingCharacterStat['CD']
            
        FinalDMG = DMG * ResMultiplier * CritMultiplier

        return FinalDMG
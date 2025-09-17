import random
import copy
import pprint


class Game:
    def __init__(self, NotNordReactionBonus=0.36):
        self.Characters = []
        self.Enemys = []

        self.BuffList = []
        self.ProportionalBuffList = []
        self.DebuffList = []
        self.AttackEffectList = []

        self._OnField = None

        self.PrintLevel = 0 # 0: 출력 안함 1: 버프, 디버프, Attack Effect 2: 공격시 스탯

    @property
    def OnField(self):
        return self._OnField if self._OnField is not None else self.Characters[0]
    
    OnField.setter
    def OnField(self, Character):
        self._OnField = Character

    def DisplayStat(self, StatType):
        for Character in self.Characters:
            if StatType == 'Base':
                Character.DisplayBaseStat()
            elif StatType == 'Buffed':
                Character.DisplayBuffedStat()
            elif StatType == 'Final':
                Character.DisplayFinalStat()
            else:
                raise ValueError

    def initCalc(self):
        self.ApplyBuffs()
        self.ApplyDebuffs()

    def AddCharacter(self, Character):
        self.Characters.append(Character)
    
    def AddEnemy(self, Enemy):
        self.Enemys.append(Enemy)

    def ApplyPartyEffect(self, NotNordCharacter=None, ElementalResonance=[], Dendro1=True, Dendro2=False):
        if NotNordCharacter is not None:
            self.AddEffect(NotNordAttackEffect(self, NotNordCharacter))
        if len(ElementalResonance) != 0:
            self.AddEffect(ElementalResonanceBuff(self, ElementalResonance, Dendro1, Dendro2))       

    def AddEffect(self, Effect):
        if Effect.Type == 'Buff':
            if not Effect.Proportional:
                self.BuffList.append(Effect)
            else:
                self.ProportionalBuffList.append(Effect)

        elif Effect.Type == 'Debuff':
            self.DebuffList.append(Effect)

        elif Effect.Type == 'AttackEffect':
            self.AttackEffectList.append(Effect)

        else:
            raise ValueError
    
    def ApplyBuffs(self):
        Print = self.PrintLevel >= 1
        for Character in self.Characters:
            Character.initBuffedStat()

        for Character in self.Characters:
            for Buff in self.BuffList:
                Buff.Apply(Character, Print)
    
        for Character in self.Characters:
            Character.initFinalStat()

        for Character in self.Characters:
            for Buff in self.ProportionalBuffList:
                Buff.Apply(Character, Print)
    
    def ApplyDebuffs(self):
        Print = self.PrintLevel >= 1
        for Enemy in self.Enemys:
            Enemy.initDebuffedStat()
        for Enemy in self.Enemys:
            for Debuff in self.DebuffList:
                Debuff.Apply(Enemy, Print)

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
        assert AttackType in ['Basic', 
                              'DirectLunarCharged', 
                              'DirectLunarBloom', 
                              'Bloom', 
                              'Burgeon', 
                              'Hyperbloom', 
                              'Burning', 
                              'Overloaded',
                              'ElectroCharged',
                              'LunarCharged',
                              'Superconduct',
                              'Swirl',
                              'Shatter']
        assert SkillType in [None, 'Normal', 'Charge', 'Plunging', 'Skill', 'Ult']
        assert DMGType in [None, 'Normal', 'Charge', 'Plunging', 'Skill', 'Ult']
        if AttackType in ['DirectLunarCharged', 'DirectLunarBloom']:
            assert DMGType == Reaction == None

        if self.PrintLevel >= 2:
            print(f'AttackName | {AttackName}')

        for AttackEffect in self.AttackEffectList:
            AttackingCharacterStatNew, TargetedEnemyStatNew = AttackEffect.Apply(AttackingCharacter, TargetedEnemy, AttackingCharacterStat.copy(), TargetedEnemyStat.copy(), AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType)
            
            if self.PrintLevel >= 2:
                for Stat in AttackingCharacterStat.keys():
                    if AttackingCharacterStat[Stat] != AttackingCharacterStatNew[Stat]:
                        change = AttackingCharacterStatNew[Stat] - AttackingCharacterStat[Stat] 
                        print(f"Effect | {AttackEffect.Name:<50} | {Stat:<25}: {change:10.3f} | {AttackingCharacterStat[Stat]:<5.3f} -> {AttackingCharacterStatNew[Stat]:<5.3f}")
                for Stat in TargetedEnemyStat.keys():
                    if TargetedEnemyStat[Stat] != TargetedEnemyStatNew[Stat]:
                        change = TargetedEnemyStatNew[Stat] - TargetedEnemyStat[Stat] 
                        print(f"Effect | {AttackEffect.Name :<50} | {Stat:<25}: {change:10.3f} | {TargetedEnemyStat[Stat]:<5.3f} -> {TargetedEnemyStatNew[Stat]:<5.3f}")

            AttackingCharacterStat, TargetedEnemyStat = AttackingCharacterStatNew, TargetedEnemyStatNew

        return AttackingCharacterStat, TargetedEnemyStat
        

    def ApplyDMG(self, AttackName, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        '''
        목표 객체에게 가하는 데미지(격변 제외)를 계산하고 적용하는 함수
        '''
        assert AttackElement in ['Physical', 'Anemo', 'Geo', 'Electro', 'Dendro', 'Hydro', 'Pyro', 'Cyro']
        assert Reaction in [None, '촉진', '발산', '융해', '증발']
        assert AttackType in ['Basic', 
                              'DirectLunarCharged', 
                              'DirectLunarBloom', 
                              'Bloom', 
                              'Burgeon', 
                              'Hyperbloom', 
                              'Burning', 
                              'Overloaded',
                              'ElectroCharged',
                              'LunarCharged',
                              'Superconduct',
                              'Swirl',
                              'Shatter']
        if AttackType in ['DirectLunarCharged', 
                        'DirectLunarBloom', 
                        'Bloom', 
                        'Burgeon', 
                        'Hyperbloom', 
                        'Burning', 
                        'Overloaded',
                        'ElectroCharged',
                        'LunarCharged',
                        'Superconduct',
                        'Swirl',
                        'Shatter']:
            assert Reaction == None
        

        if self.PrintLevel >= 3:
            HP = AttackingCharacterStat['BaseHP'] * (1 + AttackingCharacterStat['%HP']) + AttackingCharacterStat['AdditiveHP']
            ATK = AttackingCharacterStat['BaseATK'] * (1 + AttackingCharacterStat['%ATK']) + AttackingCharacterStat['AdditiveATK']
            DEF = AttackingCharacterStat['BaseDEF'] * (1 + AttackingCharacterStat['%DEF']) + AttackingCharacterStat['AdditiveDEF']

            print(f'{'AttackType':20} | {AttackType}')
            print(f'{'Multiplier':20} | {Multiplier}')
            print(f'{'Reaction':20} | {Reaction}')
            print(f'{'AttackElement':20} | {AttackElement}')
            print(f'{'Level':20} | {AttackingCharacterStat["Level"]}')
            print(f'{'HP':20} | {HP:.0f}')
            print(f'{'ATK':20} | {ATK:.0f}')
            print(f'{'DEF':20} | {DEF:.0f}')
            print(f'{'EM':20} | {AttackingCharacterStat["EM"]:.0f}')
            print(f'{'ER':20} | {AttackingCharacterStat["ER"]*100:.0f}%')
            print(f'{'CR':20} | {AttackingCharacterStat["CR"]*100:.0f}%')
            print(f'{'CD':20} | {AttackingCharacterStat["CD"]*100:.0f}%')
            print(f'{AttackElement+'DMGBonus':20} | {AttackingCharacterStat[AttackElement+'DMGBonus']*100:.0f}%')
            print(f'{'DMGBonus':20} | {AttackingCharacterStat["DMGBonus"]*100:.0f}%')
            print(f'{'BaseDMGMultiplier':20} | {AttackingCharacterStat["BaseDMGMultiplier"]*100:.0f}%')
            print(f'{'AdditiveBaseDMGBonus':20} | {AttackingCharacterStat["AdditiveBaseDMGBonus"]}')
            print(f'{'ReactionBonus':20} | {AttackingCharacterStat["ReactionBonus"]*100:.0f}%')
            print(f'{'DEFIgnored':20} | {AttackingCharacterStat["DEFIgnored"]*100:.0f}%')
            print(f'{'LunarChargedBaseDMGBonus':20} | {AttackingCharacterStat["LunarChargedBaseDMGBonus"]*100:.0f}%')
            print(f'{'LunarBloomBaseDMGBonus':20} | {AttackingCharacterStat["LunarBloomBaseDMGBonus"]*100:.0f}%')
            print(f'{'ElevatedMultiplier':20} | {AttackingCharacterStat["ElevatedMultiplier"]*100:.0f}%')
            print(f'{'TransformativeCR':20} | {AttackingCharacterStat["TransformativeCR"]*100:.0f}%')
            print(f'{'TransformativeCD':20} | {AttackingCharacterStat["TransformativeCD"]*100:.0f}%')
            print(f'{'EnemyLevel':20} | {TargetedEnemyStat["Level"]}')
            print(f'{'Enemy'+AttackElement+'Res':20} | {TargetedEnemyStat[AttackElement+'Res']*100:.0f}%')
            print(f'{'EnemyDMGReduction':20} | {TargetedEnemyStat["DMGReduction"]*100:.0f}%')
            print(f'{'EnemyDEFReduction':20} | {TargetedEnemyStat["DEFReduction"]*100:.0f}%')        
            print('\n')

        
        if AttackType == 'Basic':
            FinalDMG = self.CalcBasicDamage(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        elif AttackType == 'DirectLunarCharged':
            FinalDMG = self.CalcDirectLunarChargedDamage(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)
        
        elif AttackType == 'DirectLunarBloom':
            FinalDMG = self.CalcDirectLunarBloomDamage(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)

        elif AttackType == 'LunarCharged':
            FinalDMG = self.CalcLunarChargedDamage(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)
        
        elif AttackType in ['Bloom', 
                            'Burgeon', 
                            'Hyperbloom', 
                            'Burning', 
                            'Overloaded',
                            'ElectroCharged',
                            'LunarCharged',
                            'Superconduct',
                            'Swirl',
                            'Shatter']:
            FinalDMG = self.CalcTransformativeReactionDamage(AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier)
        
        else:
            raise ValueError        

        if self.PrintLevel >= 2:
            print(f'DMG : {FinalDMG}')   
            print('\n')

        return FinalDMG
    
    def LunarChargedDamage(self, Characters, TargetedEnemy, Print=True):
        CharacterDMGList = []
        for Character in Characters:
            LunarChargedDMG = Character.LunarCharged(TargetedEnemy)
            CharacterDMGList.append((LunarChargedDMG, Character))

        CharacterDMGList.sort(key=lambda x: x[0], reverse=True)
        
        FinalDMG = 0
        dmg_details_str_list = []

        for i, (DMG, Character) in enumerate(CharacterDMGList):
            if i == 0:
                Multiplier = 1
            elif i == 1:
                Multiplier = 0.5
            else:
                Multiplier = 1/12
            
            DealtDMG = DMG * Multiplier
            
            FinalDMG += DealtDMG
            
            Character.TotalDamageDealt += DealtDMG
            
            dmg_details_str_list.append(f'{Character.Name}: {DMG}')

        if Print:
            details_str = ", ".join(dmg_details_str_list)
            print(f'파티 총합 달감전 피해: {FinalDMG} ({details_str})')
        
        return FinalDMG

    
    def CalcBasicDamage(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        HP = AttackingCharacterStat['BaseHP'] * (1 + AttackingCharacterStat['%HP']) + AttackingCharacterStat['AdditiveHP']
        ATK = AttackingCharacterStat['BaseATK'] * (1 + AttackingCharacterStat['%ATK']) + AttackingCharacterStat['AdditiveATK']
        DEF = AttackingCharacterStat['BaseDEF'] * (1 + AttackingCharacterStat['%DEF']) + AttackingCharacterStat['AdditiveDEF']
        EM = AttackingCharacterStat['EM']
        Res = TargetedEnemyStat[f'{AttackElement}Res']

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
                raise NotImplementedError

            EMBonus = (5 * EM) / (EM + 1200)

            BaseDMG = BaseDMG + ReactionMultiplier * LevelMultiplier * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])
    
        DMGBonusMultiplier = (1 + +AttackingCharacterStat[f'{AttackElement}DMGBonus'] + AttackingCharacterStat['DMGBonus'] - TargetedEnemyStat['DMGReduction'])

        k = (1 - AttackingCharacterStat['DEFIgnored']) * (1 - TargetedEnemyStat['DEFReduction'])

        DEFMultiplier = (AttackingCharacterStat['Level'] + 100) / (k * (TargetedEnemyStat['Level'] + 100) + (AttackingCharacterStat['Level'] + 100))
        
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

        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)

        if AttackingCharacterStat['CR'] > 1.0:
            print(f'오버 치확 발생, 현재 치확: {AttackingCharacterStat["CR"]}')

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['CR']) * AttackingCharacterStat['CD']
            
        FinalDMG = BaseDMG * DMGBonusMultiplier * DEFMultiplier * AmplifyingMultiplier * ResMultiplier * CritMultiplier

        return FinalDMG
    
    def CalcDirectLunarChargedDamage(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        HP = AttackingCharacterStat['BaseHP'] * (1 + AttackingCharacterStat['%HP']) + AttackingCharacterStat['AdditiveHP']
        ATK = AttackingCharacterStat['BaseATK'] * (1 + AttackingCharacterStat['%ATK']) + AttackingCharacterStat['AdditiveATK']
        DEF = AttackingCharacterStat['BaseDEF'] * (1 + AttackingCharacterStat['%DEF']) + AttackingCharacterStat['AdditiveDEF']
        EM = AttackingCharacterStat['EM']
        Res = TargetedEnemyStat[f'{AttackElement}Res']

        BaseDMG = HP * Multiplier['HP'] + ATK * Multiplier['ATK'] + DEF * Multiplier['DEF'] + EM * Multiplier['EM']
            
        BaseDMG = BaseDMG * (1 + AttackingCharacterStat['LunarChargedBaseDMGBonus'])

        EMBonus = (6 * EM) / (EM + 2000)

        BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)

        if AttackingCharacterStat['CR'] > 1.0:
            print(f'오버 치확 발생, 현재 치확: {AttackingCharacterStat["CR"]}')

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['CR']) * AttackingCharacterStat['CD']

        FinalDMG = 3 * BaseDMG * ResMultiplier * CritMultiplier * (1 + AttackingCharacterStat['ElevatedMultiplier'])

        return FinalDMG
    
    def CalcLunarChargedDamage(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        EM = AttackingCharacterStat['EM']
        Res = TargetedEnemyStat[f'{AttackElement}Res']

        if AttackingCharacterStat['Level'] == 90:
            LevelMultiplier = 1446.8535
        elif AttackingCharacterStat['Level'] == 95:
            LevelMultiplier = 1561.468
        elif AttackingCharacterStat['Level'] == 100:
            LevelMultiplier = 1674.8092
        else:
            raise NotImplementedError
        
        BaseDMG = 1.8 * LevelMultiplier

        BaseDMG = BaseDMG * (1 + AttackingCharacterStat['LunarChargedBaseDMGBonus'])

        EMBonus = (6 * EM) / (EM + 2000)

        BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)

        if AttackingCharacterStat['CR'] > 1.0:
            print(f'오버 치확 발생, 현재 치확: {AttackingCharacterStat["CR"]}')

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['CR']) * AttackingCharacterStat['CD']

        FinalDMG = BaseDMG * ResMultiplier * CritMultiplier * (1 + AttackingCharacterStat['ElevatedMultiplier'])

        return FinalDMG
    
    def CalcDirectLunarBloomDamage(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        HP = AttackingCharacterStat['BaseHP'] * (1 + AttackingCharacterStat['%HP']) + AttackingCharacterStat['AdditiveHP']
        ATK = AttackingCharacterStat['BaseATK'] * (1 + AttackingCharacterStat['%ATK']) + AttackingCharacterStat['AdditiveATK']
        DEF = AttackingCharacterStat['BaseDEF'] * (1 + AttackingCharacterStat['%DEF']) + AttackingCharacterStat['AdditiveDEF']
        EM = AttackingCharacterStat['EM']
        Res = TargetedEnemyStat[f'{AttackElement}Res']

        BaseDMG = HP * Multiplier['HP'] + ATK * Multiplier['ATK'] + DEF * Multiplier['DEF'] + EM * Multiplier['EM']

        BaseDMG = BaseDMG * (1 + AttackingCharacterStat['LunarBloomBaseDMGBonus'])

        BaseDMG = BaseDMG * (1 + AttackingCharacterStat['BaseDMGMultiplier'])

        EMBonus = (6 * EM) / (EM + 2000)

        BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

        BaseDMG = BaseDMG + AttackingCharacterStat['AdditiveBaseDMGBonus']

        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)

        if AttackingCharacterStat['CR'] > 1.0:
            print(f'오버 치확 발생, 현재 치확: {AttackingCharacterStat["CR"]}')

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['CR']) * AttackingCharacterStat['CD']

        FinalDMG = BaseDMG * ResMultiplier * CritMultiplier * (1 + AttackingCharacterStat['ElevatedMultiplier'])

        return FinalDMG
    
    def CalcTransformativeReactionDamage(self, AttackingCharacterStat, TargetedEnemyStat, AttackElement, Reaction, AttackType, Multiplier):
        EM = AttackingCharacterStat['EM']
        Res = TargetedEnemyStat[f'{AttackElement}Res']

        if AttackingCharacterStat['Level'] == 90:
            LevelMultiplier = 1446.8535
        elif AttackingCharacterStat['Level'] == 95:
            LevelMultiplier = 1561.468
        elif AttackingCharacterStat['Level'] == 100:
            LevelMultiplier = 1674.8092
        else:
            raise NotImplementedError
        
        if AttackType == 'Burning':
            ReactionMultiplier = 0.25
        elif AttackType == 'Swirl':
            ReactionMultiplier = 0.6
        elif AttackType == 'Superconduct':
            ReactionMultiplier = 1.5
        elif AttackType == 'ElectroCharged':
            ReactionMultiplier = 2.0
        elif AttackType == 'Bloom':
            ReactionMultiplier = 2.0
        elif AttackType == 'Overloaded':
            ReactionMultiplier = 2.75
        elif AttackType == 'Burgeon':
            ReactionMultiplier = 3.0
        elif AttackType == 'Hyperbloom':
            ReactionMultiplier = 3.0
        elif AttackType == 'Shatter':
            ReactionMultiplier = 3.0
        else:
            raise ValueError

        BaseDMG = ReactionMultiplier * LevelMultiplier

        EMBonus = (6 * EM) / (EM + 2000)

        BaseDMG = BaseDMG * (1 + EMBonus + AttackingCharacterStat['ReactionBonus'])

        BaseDMG = BaseDMG + AttackingCharacterStat['AdditiveBaseDMGBonus']

        if Res < 0 :
            ResMultiplier = 1 - (Res / 2)
        elif Res >=0 and Res < 0.75 :
            ResMultiplier = 1 - Res
        else:
            ResMultiplier = 1 / (4 * Res + 1)
        

        CritMultiplier = 1 + min(1.0, AttackingCharacterStat['TransformativeCR']) * AttackingCharacterStat['TransformativeCD']

        FinalDMG = BaseDMG * ResMultiplier * CritMultiplier

        return FinalDMG
    
class NotNordAttackEffect: 
    def __init__(self, Game, Character):
        self.Name = 'Not Nord LunarDMGBonus'
        self.Type = 'AttackEffect'

        self.Game =Game
        self.Character = Character


    def Apply(self, AttackingCharacter, TargetedEnemy, AttackingCharacterStat, TargetedEnemyStat, AttackName, AttackElement, Reaction, AttackType, SkillType, DMGType):
        if AttackType in ['DirectLunarCharged', 'DirectLunarBloom', 'LunarCharged']:
            HP = self.Character.FinalStat['BaseHP'] * (1 + self.Character.FinalStat['%HP']) + self.Character.FinalStat['AdditiveHP']
            ATK = self.Character.FinalStat['BaseATK'] * (1 + self.Character.FinalStat['%ATK']) + self.Character.FinalStat['AdditiveATK']
            DEF = self.Character.FinalStat['BaseDEF'] * (1 + self.Character.FinalStat['%DEF']) + self.Character.FinalStat['AdditiveDEF']
            EM = self.Character.FinalStat['EM']

            if self.Character.Element in ['Pyro', 'Cyro', 'Electro']:
                Amount = min(0.36, ATK/100 * 0.012)
            elif self.Character.Element in ['Anemo', 'Dendro']:
                Amount = min(0.36, EM/100 * 0.03)
            elif self.Character.Element == 'Hydro':
                Amount = min(0.36, HP/1000 * 0.008)
            elif self.Character.Element == 'Geo':
                Amount = min(0.36, DEF/100 * 0.012)
    
            AttackingCharacterStat['ReactionBonus']  += Amount
    
        return AttackingCharacterStat, TargetedEnemyStat

class ElementalResonanceBuff: # (범용상황, 범용버프) + (범용상황, 특정버프) + (특정상황, 특정버프) 
    def __init__(self, Game, ElementalResonances, Dendro1=True, Dendro2=False):
        self.Name = 'ElementalResonanceBuff'
        self.Proportional = False
        self.Type = 'Buff'

        self.Game = Game
        self.ElementalResonances = ElementalResonances
        self.Dendro1 = Dendro1
        self.Dendro2 = Dendro2

    def Apply(self, BuffedCharacter, Print):
        for Element in self.ElementalResonances:
            if Element == 'Pyro':
                Stat = '%ATK'
                Amount = 0.25
                BuffedCharacter.BuffedStat[Stat] += Amount  
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            elif Element == 'Hydro':
                Stat = '%HP'
                Amount = 0.25
                BuffedCharacter.BuffedStat[Stat] += Amount  
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            elif Element == 'Cyro':
                Stat = 'CR'
                Amount = 0.15
                BuffedCharacter.BuffedStat[Stat] += Amount  
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            elif Element == 'Dendro':
                Stat = 'EM'
                Amount = 50 
                if self.Dendro1 == True:
                    Amount += 30
                if self.Dendro2 == True:
                    Amount += 20
                BuffedCharacter.BuffedStat[Stat] += Amount  
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            elif Element == 'Geo':
                Stat = 'DMGBonus'
                Amount = 0.15
                BuffedCharacter.BuffedStat[Stat] += Amount  
                if Print:
                    print(f"Buff   | {self.Name:<40} | {BuffedCharacter.Name:<20} | {Stat:<25}: +{Amount:<8.3f} | -> {BuffedCharacter.BuffedStat[Stat]:<5.3f}")
            else:
                raise ValueError

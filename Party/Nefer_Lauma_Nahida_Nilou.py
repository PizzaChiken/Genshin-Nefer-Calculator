import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from Game import Game
from BaseEnemy import BaseEnemyClass
from Characters.Nefer import NeferClass
from Characters.Lauma import LaumaClass
from Characters.Nahida import NahidaClass
from Characters.Nilou import NilouClass

from Weapons.Catalyst.ReliquaryofTruth import ReliquaryofTruth
from Weapons.Catalyst.AThousandFloatingDreams import AThousandFloatingDreams
from Weapons.Catalyst.NightweaversLookingGlass import NightweaversLookingGlass
from Weapons.Sword.KeyofKhajNisut import KeyofKhajNisut

from Artifacts.NightOfTheSkysUnveiling import NightOfTheSkysUnveiling
from Artifacts.SilkenMoonsSerenade import SilkenMoonsSerenade
from Artifacts.DeepwoodMemories import DeepwoodMemories

# 부옵 규칙
# 1. 옵션 5개 골라서 2개씩 (10개)
# 2. 2개 옵션 합이 22개 넘으면 안됨
# 3. 개별 옵션 개수는 가능한 부위 * 3을 넘으면 안됨
# {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*0, 'CR':0.033*0, 'CD':0.066*0},

# 1. 게임 초기화
Calculator = Game()
Calculator.PrintLevel = 0 # 0: 출력 안함 1: 버프, 디버프, 2: Attack Effect 3: 공격시 스탯

# 2. 적 추가
Enemy = BaseEnemyClass(Calculator)
Calculator.AddEnemy(Enemy)

# 3. 캐릭터 1 추가
NeferConstellation = 2
NeferRefinements = 1
Nefer = NeferClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=NeferConstellation)
Nefer.AddWeapon(ReliquaryofTruth(Calculator, Nefer, NeferRefinements, LunarBloomActive=True, SkillActive=True))
Nefer.AddArtifactSet(NightOfTheSkysUnveiling(Calculator,Nefer, PC=4))
Nefer.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*2, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*1}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*2, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*2, '%DEF':0.062*0, 'EM':20*6, 'ER':0.055*0, 'CR':0.033*8, 'CD':0.066*12}, # 부옵
    ]) 
Calculator.AddCharacter(Nefer)

# 4. 캐릭터 2 추가
LaumaConstellation = 2
LaumaRefinements = 1
Lauma = LaumaClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=LaumaConstellation)
Lauma.AddWeapon(NightweaversLookingGlass(Calculator, Lauma, LaumaRefinements, SkillActive=True, LunarBloomActive=True))
Lauma.AddArtifacts([
    {'EM' : 160}, # 원마 22셋
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*3, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*2, '%DEF':0.062*0, 'EM':20*6, 'ER':0.055*8, 'CR':0.033*10, 'CD':0.066*4},
    ]) 
Calculator.AddCharacter(Lauma)

# 5. 캐릭터 3 추가
NahidaConstellation = 2
NahidaRefinements = 1
Nahida = NahidaClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=NahidaConstellation, CatalyzeActive=False, C4Cnt=1)
Nahida.AddWeapon(AThousandFloatingDreams(Calculator, Nahida, NahidaRefinements, Cnt=[2, 1]))
Nahida.AddArtifactSet(DeepwoodMemories(Calculator, Nahida, PC=4))
Nahida.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*2, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*1, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*2, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*8, 'CR':0.033*8, 'CD':0.066*10},
    ]) 
Calculator.AddCharacter(Nahida)

# 6. 캐릭터 4 추가
NilouConstellation = 0
NilouRefinements = 1
Nilou = NilouClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=NilouConstellation, P1Active=False)
Nilou.AddWeapon(KeyofKhajNisut(Calculator, Nilou, NilouRefinements))
Lauma.AddArtifactSet(SilkenMoonsSerenade(Calculator, Nilou, PC=4))
Nilou.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*3, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*0, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*15, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*6, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*0, 'CR':0.033*5, 'CD':0.066*2},
    ]) 
Calculator.AddCharacter(Nilou)

# 7. 파티효과 적용
Calculator.ApplyPartyEffect(NotNordCharacter=Nilou, ElementalResonance=['Dendro'], Dendro1=True)
Calculator.OnField = Nefer

#8. 파티버프 발동
Calculator.initCalc()


#9. 캐릭터 스탯 표시
Calculator.DisplayStat('Final')


# 10. 피해 계산
TotalDMG = 0

TotalDMG += Nefer.Roatation(Enemy)
TotalDMG += Lauma.Rotation(Enemy, EHold=False, Stack=0, Count=8)
TotalDMG += Nahida.Rotation(Enemy, Count=9, Reaction=None)
TotalDMG += Nilou.Rotation(Enemy)


# 11. 결과 표시
print('\n')
print(f'{'네페르':8} {NeferConstellation}돌 {NeferRefinements}재, 사이클데미지: {Nefer.TotalDamageDealt:.0f}')
print(f'{'라우마':8} {LaumaConstellation}돌 {LaumaRefinements}재, 사이클데미지: {Lauma.TotalDamageDealt:.0f}')
print(f'{'나히다':8} {NahidaConstellation}돌 {NahidaRefinements}재, 사이클데미지: {Nahida.TotalDamageDealt:.0f}')
print(f'{'닐루':8} {NilouConstellation}돌 {NilouRefinements}재, 사이클데미지: {Nilou.TotalDamageDealt:.0f}')
print(f'파티 사이클 데미지 : {TotalDMG:.0f}')






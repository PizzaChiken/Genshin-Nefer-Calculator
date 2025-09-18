import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from Game import Game
from BaseEnemy import BaseEnemyClass

from Characters.Flins import FlinsClass
from Characters.Ineffa import IneffaClass
from Characters.Aino import AinoClass
from Characters.Bennett import BennettClass

from Weapons.Polearm.BloodsoakedRuins import BloodsoakedRuins
from Weapons.Polearm.FracturedHalo import FracturedHalo
from Weapons.Claymore.FlameForgedInsight import FlameForgedInsight
from Weapons.Sword.AquilaFavonia import AquilaFavonia

from Artifacts.NightOfTheSkysUnveiling import NightOfTheSkysUnveiling
from Artifacts.SilkenMoonsSerenade import SilkenMoonsSerenade
from Artifacts.NoblesseOblige import NoblesseOblige

# 부옵 규칙
# 1. 옵션 5개 골라서 2개씩 (10개)
# 2. 2개 옵션 합이 22개 넘으면 안됨
# 3. 개별 옵션 개수는 가능한 부위 * 3을 넘으면 안됨
"""
.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*0, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*0, 'CR':0.033*0, 'CD':0.066*0},
    ]) 
"""

# 1. 게임 초기화
Calculator = Game()
Calculator.PrintLevel = 0 # 0: 출력 안함 1: 버프, 디버프, 2: Attack Effect 3: 공격시 스탯

# 2. 적 추가
Enemy = BaseEnemyClass(Calculator)
Calculator.AddEnemy(Enemy)

# 3. 캐릭터 1 추가
FlinsConstellation = 6
FlinsRefinements = 5
Flins = FlinsClass(Calculator, Constellation=FlinsConstellation, thunderclouds=True)
Flins.AddWeapon(BloodsoakedRuins(Calculator, Flins, FlinsRefinements, UltActive=True, LunarChargedActive=True))
Flins.AddArtifactSet(NightOfTheSkysUnveiling(Calculator, Flins, PC=4))
Flins.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*2, '%DEF':0.583*0, 'EM':187*0, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*1}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*2, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*4, 'CR':0.033*13, 'CD':0.066*9},
    ]) 
Calculator.AddCharacter(Flins)

# 4. 캐릭터 2 추가
IneffaConstellation = 6
IneffaRefinements = 5
Ineffa = IneffaClass(Calculator, Constellation=IneffaConstellation, thunderclouds=True, UltActive=True)
Ineffa.AddWeapon(FracturedHalo(Calculator, Ineffa, IneffaRefinements, SkillActive=True, ShieldActive=True))
Ineffa.AddArtifacts([
    {'EM' : 160}, # 원마 22셋
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*2, '%DEF':0.583*0, 'EM':187*0, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*1, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*4, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*2, 'CR':0.033*11, 'CD':0.066*11},
    ]) 
Calculator.AddCharacter(Ineffa)

# 5. 캐릭터 3 추가

AinoConstellation = 6
AinoRefinements = 5
Aino = AinoClass(Calculator, Constellation=AinoConstellation, C1Active=True)
Aino.AddWeapon(FlameForgedInsight(Calculator, Aino, AinoRefinements, ReactionActive=True))
Aino.AddArtifactSet(SilkenMoonsSerenade(Calculator, Aino, PC=4))
Aino.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*3, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*0, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*2, '%DEF':0.062*0, 'EM':20*6, 'ER':0.055*6, 'CR':0.033*8, 'CD':0.066*8},
    ]) 
Calculator.AddCharacter(Aino)


# 6. 캐릭터 4 추가
BennettConstellation = 6
BennettRefinements = 5
Bennett = BennettClass(Calculator, Constellation=BennettConstellation)
Bennett.AddWeapon(AquilaFavonia(Calculator, Bennett, BennettRefinements))
Bennett.AddArtifactSet(NoblesseOblige(Calculator, Bennett, PC=4))
Bennett.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*2, '%DEF':0.583*0, 'EM':187*0, 'ER':0.518*1, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'AdditiveHP':254*0, 'AdditiveATK':17*2, 'AdditiveDEF':20*0, '%HP':0.050*0, '%ATK':0.050*9, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*12, 'CR':0.033*5, 'CD':0.066*2},
    ]) 
Calculator.AddCharacter(Bennett)


# 7. 파티효과 적용
Calculator.ApplyPartyEffect(NotNordCharacter=Bennett, ElementalResonance=['Electro'])
Calculator.OnField = Flins

#8. 파티버프 발동
Calculator.initCalc()


#9. 캐릭터 스탯 표시
Calculator.DisplayStat('Final')


# 10. 피해 계산
TotalDMG = 0


# 10. 피해 계산
TotalDMG = 0

TotalDMG += Flins.Rotation(Enemy)
TotalDMG += Ineffa.Rotation(Enemy, BirgitaCount=8, C6Count=4)
TotalDMG += Aino.Rotation(Enemy)
TotalDMG += Bennett.Rotation(Enemy)
TotalDMG += Calculator.LunarChargedDamageRotation([Flins, Ineffa, Aino], Enemy, Count=8)

# 11. 결과 표시
print('\n')
print(f'{'플린스':8} {FlinsConstellation}돌 {FlinsRefinements}재, 사이클데미지: {Flins.TotalDamageDealt:.0f}')
print(f'{'이네파':8} {IneffaConstellation}돌 {IneffaRefinements}재, 사이클데미지: {Ineffa.TotalDamageDealt:.0f}')
print(f'{'아이노':8} {AinoConstellation}돌 {AinoRefinements}재, 사이클데미지: {Aino.TotalDamageDealt:.0f}')
print(f'{'베넷':8} {BennettConstellation}돌 {BennettRefinements}재, 사이클데미지: {Bennett.TotalDamageDealt:.0f}')
print(f'파티 사이클 데미지 : {TotalDMG:.0f}')






from Game import Game
from BaseEnemy import BaseEnemyClass
from Characters.네페르 import NeferClass
from Characters.나히다 import AddNahidaTemp
from Characters.라우마 import LaumaClass
from Characters.닐루 import AddNilouTemp

from Weapons.네페르전무 import NeferSignature
from Weapons.나히다전무 import AddNahidaSignatureTemp, NahidaSignature
from Weapons.라우마전무 import LaumaSignature
from Weapons.닐루전무 import AddNilouSignatureTemp

from Artifacts.하늘경계가드러난밤 import NightOfTheSkysUnveiling
from Artifacts.달을엮는밤노래 import SilkenMoonsSerenade
from Artifacts.숲의기억 import AddDeepwoodMemorieTemp

from Party.비노드버프 import AddNotNordTemp


Calculator = Game()
Calculator.PrintAll = False # 디버깅용, 현재 데미지에 적용중인 버프들, 현재 데미지 계산시 캐릭터 스탯 등등을 print

Enemy = BaseEnemyClass(Calculator)
Calculator.AddEnemy(Enemy)

# 네페르
NeferConstellation = 0
NeferRefinements = 0
Nefer = NeferClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=NeferConstellation)
Nefer.AddWeapon(NeferSignature(Nefer, NeferRefinements))
Nefer.AddArtifactSet(NightOfTheSkysUnveiling(Nefer, PC=4, Moonsign=2))
Nefer.AddArtifacts([
    {'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*2, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*1}, # 주옵
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*0, 'CR':0.033*3, 'CD':0.066*2}, # 슬롯1
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*0, 'CR':0.033*3, 'CD':0.066*2}, # 슬롯2
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*0, 'CR':0.033*3, 'CD':0.066*2}, # 슬롯3
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*0, 'CR':0.033*3, 'CD':0.066*2}, # 슬롯4
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*3, 'ER':0.055*0, 'CR':0.033*2, 'CD':0.066*0}, # 슬롯5
    ]) 
Calculator.AddCharacter(Nefer)
#Nefer.DisplayBaseStat()

# 라우마
LaumaConstellation = 6
LaumaRefinements = 5
Lauma = LaumaClass(Calculator, Level=90, SkillLevel={'Normal' : 10, 'Skill' : 10, 'Ult' : 10}, Constellation=LaumaConstellation, Moonsign=2)
Lauma.AddWeapon(LaumaSignature(Lauma, LaumaRefinements))
Lauma.AddArtifactSet(SilkenMoonsSerenade(Lauma, PC=4, Moonsign=2))
Lauma.AddArtifacts([
{'AdditiveHP':4780, 'AdditiveATK':311, '%HP':0.466*0, '%ATK':0.466*0, '%DEF':0.583*0, 'EM':187*3, 'ER':0.518*0, 'DendroDMGBonus':0.466*0, 'PhysicalDMGBonus':0.583*0, 'CR':0.311*0, 'CD':0.622*0}, # 주옵
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*3, 'CR':0.033*0, 'CD':0.066*0}, # 슬롯1
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*2, 'ER':0.055*3, 'CR':0.033*0, 'CD':0.066*0}, # 슬롯2
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*3, 'CR':0.033*0, 'CD':0.066*0}, # 슬롯3
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*3, 'CR':0.033*0, 'CD':0.066*0}, # 슬롯4
    {'%HP':0.050*0, '%ATK':0.050*0, '%DEF':0.062*0, 'EM':20*0, 'ER':0.055*3, 'CR':0.033*0, 'CD':0.066*0}, # 슬롯5
    ]) 
Calculator.AddCharacter(Lauma)

# 나히다
NahidaConstellation = 0
NahidaRefinements = 1
AddNahidaTemp(Calculator, Constellation=NahidaConstellation, EM=1000, CatalyzeActive=False)
AddNahidaSignatureTemp(Calculator, Refinements=NahidaRefinements)
AddDeepwoodMemorieTemp(Calculator, PC=4)


# 닐루
NilouConstellation = 0
NilouRefinements = 1
AddNilouTemp(Calculator, Constellation=NilouConstellation, P1EMActive=False)
AddNilouSignatureTemp(Calculator, Refinements=NilouRefinements, HP=74444)

#비노드버프
AddNotNordTemp(Calculator, 0.36)

Calculator.initCalc()

TotalDMG = 0
TotalDMG += Nefer.SkillCACombine(Enemy)
TotalDMG += Nefer.SkillCACombine(Enemy, Print=False)
TotalDMG += Nefer.SkillCACombine(Enemy, Print=False)
TotalDMG += Nefer.SkillCACombine(Enemy, Print=False)
TotalDMG += Nefer.SkillCACombine(Enemy, Print=False)
TotalDMG += Nefer.SkillCACombine(Enemy, Print=False)


print('\n')
print(f'네페르 {NeferConstellation}돌 {NeferRefinements}재')
print(f'나히다 {NahidaConstellation}돌 {NahidaRefinements}재')
print(f'라우마 {LaumaConstellation}돌 {LaumaRefinements}재')
print(f'닐루 {NilouConstellation}돌 {NilouRefinements}재')
print(f'총 데미지 : {TotalDMG}')





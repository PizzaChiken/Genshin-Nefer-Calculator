
class BaseEnemyClass:
    def __init__(self, Game, Level=100, Res=0.1):
        self.Name = 'TestEnemy'
        self.Game = Game
        
        self.BaseStat = {
                'Level' : Level,
                'PhysicalRes' : Res,
                'AnemoRes' : Res,
                'GeoRes' : Res,
                'ElectroRes' : Res,
                'DendroRes' : Res,
                'HydroRes' : Res,
                'PyroRes' : Res,
                'CyroRes' : Res,
                'DMGReduction' : 0,
                'DEFReduction' : 0,
            }
    
    def initDebuffedStat(self):
        self.DebuffedStat = self.BaseStat.copy()
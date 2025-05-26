from LeaguePlayer import LeaguePlayer

class NationalPlayer(LeaguePlayer):
    def __init__(self, firstName, lastName, age, nation,
                 branch, game_num, win_num, lost_num, player_score,
                 nationalGame_num, nationalPlayer_score):
        super().__init__(firstName, lastName, age, nation,
                     branch, game_num, win_num, lost_num, player_score)
        self.ngn = nationalGame_num
        self.nps = nationalPlayer_score
        
    def set_nationalGame_num(self, x):
        self.ngn = x
        
    def set_nationalPlayer_score(self, x):
        self.nps = x
        
    def get_nationalGame_num(self):
        return self.ngn
    
    def get_nationalPlayer_score(self):
        return self.nps
    
    def print_player(self):
        super().print_player()
        print(" national game num: ", self.get_nationalGame_num())
        print(" national player score: ", self.get_nationalPlayer_score())
        
    def statistic(self):
        statistic = self.get_nationalPlayer_score() / self.get_nationalGame_num()
        print("national statistic: ", statistic)
        
    def points(self):
        points = (15*self.get_nationalGame_num()) + super().points()
        print("league points: ", super().points())
        print("national points: ", points)
        
        
    
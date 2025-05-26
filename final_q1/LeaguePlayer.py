from Player import Player

class LeaguePlayer(Player):
    def __init__(self, firstName, lastName, age, nation,
                 branch, game_num, win_num, lost_num, player_score):
        Player.__init__(self, firstName, lastName, age, nation)
        self.b = branch
        self.wn = win_num
        self.gn = game_num
        self.ln = lost_num
        self.ps = player_score
        
    def set_branch(self, x):
        self.b = x
        
    def set_gameNum(self, x):
        self.gn = x
        
    def set_winNum(self, x):
        self.wn = x
        
    def set_lostNum(self, x):
        self.ln = x
        
    def set_playerScore(self, x):
        self.ps = x
        
    def get_branch(self):
        return self.b
    
    def get_gameNum(self):
        return self.gn
    
    def get_winNum(self):
        return self.wn
    
    def get_lostNum(self):
        return self.ln
    
    def get_playerScore(self):
        return self.ps
    
    def print_player(self):
        super().print_player()
        print("branch: ", self.get_branch())
        print("game num: ", self.get_gameNum())
        print("win num: ",self.get_winNum())
        print("lost num: ", self.get_lostNum())
        print("player score: ", self.get_playerScore())
        
    def statistics(self):
        statistic = self.get_playerScore() / self.get_gameNum()
        print("statistic: ", statistic)
        
    def points(self):
        points = (10*self.get_gameNum()) + (3*self.get_winNum()) - (2*self.get_lostNum())
        return points        
        
        
        
        
        
    
    
    
    
    
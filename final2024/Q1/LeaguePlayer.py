from Player import Player

class LeaguePlayer(Player):
    def __init__(self, firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score):
        super().__init__(firstName, lastName, age, nation)
        self.__branch = branch
        self.__game_num = game_num
        self.__win_num = win_num
        self.__lost_num = lost_num
        self.__player_score = player_score
        
    def set_branch(self,branch):
        self.__branch = branch
        
    def get_branch(self):
        return self.__branch
    
    
    def set_game_num(self,game_num):
        self.__game_num = game_num
        
    def get_game_num(self):
        return self.__game_num
    
    
    def set_win_num(self,win_num):
        self.__win_num = win_num
        
    def get_win_num(self):
        return self.__win_num
    
    
    def set_lost_num(self,lost_num):
        self.__lost_num = lost_num
        
    def get_lost_num(self):
        return self.__lost_num
    
    
    def set_player_score(self,player_score):
        self.__player_score = player_score
        
    def get_player_score(self):
        return self.__player_score
    
    def print_player(self):
        super().print_player()
        print("branch:",self.get_branch())
        print("game num: ", self.get_game_num())
        print("win num: ",self.get_win_num())
        print("lost num: ",self.get_lost_num())
        print("player score: ",self.get_player_score())
        
    def statistics(self):
        statistics_result = get_player_score()/ get_game_num()
        print("statistics result: ",statistics_result)
        
    def points(self):
        points_result = (10*self.get_game_num()) +( 3*self.get_win_num()) - (2*self.get_lost_num())
        return points_result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
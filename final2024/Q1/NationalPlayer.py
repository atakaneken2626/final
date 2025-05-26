from LeaguePlayer import LeaguePlayer


class NationalPlayer(LeaguePlayer):
    def __init__(self, firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score, nationalGame_num, nationalPlayer_score):
        super().__init__(firstName, lastName, age, nation, branch, game_num, win_num, lost_num, player_score)
        self.__nationalGame_num = nationalGame_num
        self.__nationalPlayer_score = nationalPlayer_score
        
    def set_nationalGame_num(self,nationalGame_num):
        self.__nationalGame_num = nationalGame_num
        
    def get_nationalGame_num(self):
        return self.__nationalGame_num
    
    
    def set_nationalPlayer_score(self,nationalPlayer_score):
        self.__nationalPlayer_score = nationalPlayer_score
        
    def get_nationalPlayer_score(self):
        return self.__nationalPlayer_score
    
    
    def print_player(self):
        super().print_player()
        print("National Game Number:",self.get_nationalGame_num())
        print("National Player Score: ", self.get_nationalPlayer_score())

    def statistics(self):
        statistics_result = get_nationalPlayer_score()/ get_nationalGame_num()
        print("statistics result: ",statistics_result)
        
    def points(self):
        points = (15*self.get_nationalGame_num()) + super().points()
        print("points:",points)
                    
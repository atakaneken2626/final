from Player import Player
from LeaguePlayer import LeaguePlayer
from NationalPlayer import NationalPlayer

# Player 1: Sadece Player sınıfı
p1 = Player("Fabian", "Delph", 22, "England")
p1.print_player()
print()

# Player 2: LeaguePlayer
p2 = LeaguePlayer("Tony", "Parker", 28, "France",
                  "Basketball", 36, 19, 6, 22)
p2.print_player()
#print("Scores per league game:", round(p2.get_player_score() / p2.get_gameNum(), 2))
print("Player points:", p2.points())
print()

# Player 3: NationalPlayer
p3 = NationalPlayer("Jordan", "Larson", 22, "USA",
                    "Volleyball", 21, 16, 4, 36,
                    8, 3)
p3.print_player()
print("Player points:", p3.points())

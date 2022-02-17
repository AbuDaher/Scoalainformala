# 2. Functia map
# Rolul acestei functii este de a modifica fiecare element al unei liste.
import copy

players = [{
    "first_name": "Ion",
    "second_name": "Popescu",
    "rank": 3
}, {
    "first_name" : "Maria",
    "second_name": "Ionescu",
    "rank": 6
}, {
    "first_name": "Ianis",
    "second_name": "Vasile",
    "rank": 1
}]

def check_top_3_players(player):
    updated_player = copy.deepcopy(player)
    updated_player["is top 3"] = True if updated_player["rank"] <= 3 else False
    return updated_player
    players_with_top_3_value = map(check_top_3_players, players)
    print("players_with_top_3_value=", list(players_with_top_3_value))

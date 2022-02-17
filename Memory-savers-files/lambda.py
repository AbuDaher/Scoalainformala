# 1. Functia lambda
# Scopul este de a eficientiza scrierea, salvand timp si memorie
#Este o functie anonima care indeplineste o singura intructiune dar poate primi un numar nedefinit de parametri.
my_function = lambda x, y: x * y
produs = my_function(2, 5)
print(f"Produsul meu este {produs} ")


players = [{
    "first_name": "Ion",
    "second_name": "Popescu",
    "varsta": 25
}, {
    "first_name" : "Maria",
    "second_name": "Ionescu",
    "varsta": 44
}, {
    "first_name": "Ianis",
    "second_name": "Vasile",
    "varsta": 16
}]
sorted_players = sorted(players, key=lambda player: player["varsta"])
print(sorted_players)
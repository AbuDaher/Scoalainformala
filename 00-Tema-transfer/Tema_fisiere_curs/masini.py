# Still work in progress, any advice will be strongly appreciated :D

import copy
import random
import pandas as pd
import json


dict_masini = [
    {
        "id": "-",
        "brand": "Audi",
        "model": "A7",
        "hp": 362,
        "price": 7000
    },
    {
            "id": "-",
            "brand": "BMW",
            "model": "I4",
            "hp": 250,
            "price": 5000
        },
    {
            "id": "-",
            "brand": "Honda",
            "model": "Sedan",
            "hp": 175,
            "price": 4500
        },
    {
            "id": "-",
            "brand": "Lexus",
            "model": "UX",
            "hp": 142,
            "price": 3400
        },
    {
            "id": "-",
            "brand": "Kia",
            "model": "Sorento",
            "hp": 85,
            "price": 850
        },
    {
            "id": "-",
            "brand": "Mercedes",
            "model": "C Class",
            "hp": 275,
            "price": 6450
        },
    {
            "id": "-",
            "brand": "Tesla",
            "model": "X",
            "hp": 590,
            "price": 1150
        },
    {
            "id": "-",
            "brand": "Toyota",
            "model": "Yaris",
            "hp": 110,
            "price": 950
        },
    {
            "id": "-",
            "brand": "Skoda",
            "model": "Fabia",
            "hp": 90,
            "price": 900
    }]
for i in range(9):
    if dict_masini[i]["id"] == "-":
        dict_masini[i]["id"] = random.randint(111, 999)
variabila = pd.DataFrame(dict_masini)
fisier = variabila.to_csv("input.csv")

csv_py = pd.read_csv("input.csv")
print(csv_py)


def range_car_hp(car):
    update_status_hp = copy.deepcopy(car)
    update_status_hp["slow_cars"] = True if update_status_hp["hp"] < 120 else False
    update_status_hp["fast_cars"] = True if 120 <= update_status_hp["hp"] < 180 else False
    update_status_hp["sport_cars"] = True if update_status_hp["hp"] >= 180 else False
    return update_status_hp


status_hp = map(range_car_hp, dict_masini)
variabila1 = pd.DataFrame(status_hp)
new_dict_masini = variabila1.to_dict()
fisier1 = variabila1.to_json("output_data/export_hp.json")


def filter_car_hp(car):
    if car["slow_cars"] == 1:
        return True
    elif car["fast_cars"] == 1:
        return True
    else:
        return True


x = filter(filter_car_hp, new_dict_masini)
print(x)


def range_car_price(car):
    update_status_price = copy.deepcopy(car)
    update_status_price["cheap"] = True if update_status_price["price"] < 1000 else False
    update_status_price["medium"] = True if 1000 <= update_status_price["price"] < 5000 else False
    update_status_price["expensive"] = True if update_status_price["price"] >= 5000 else False
    return update_status_price


status_price = map(range_car_price, dict_masini)
variabila2 = pd.DataFrame(status_price)
new_dict_masini2 = variabila2.to_dict()
fisier2 = variabila2.to_json("output_data/export_price.json")


def filter_car_price(car):
    if car["cheap"] == 1:
        return True
    elif car["medium"] == 1:
        return True
    else:
        return True


y = filter(filter_car_price, new_dict_masini2)
print(x)


json_string = json.dumps(dict_masini)
with open("output_data/fisier.json", "w") as outfile:
    json.dump(json_string, outfile)

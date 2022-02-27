
# Still work in progress, any advice will be strongly appreciated :D

import csv
categorie = []
activitati = []
responsabil = []
termen = []
asignare = []
input_activ = True


def categorii():

    n = int(input("Introdu numaru de categorii pe care vrei sa le introduci: "))
    for i in range(0, n):
        input_categorii = input("Introdu categoria dorita: ")
        categorie.append(input_categorii)
        # print(categorie)


categorii()


def input_values():
    input_activitate = input("Introdu task-ul: ")
    input_termen = input("Introdu deadline-ul: ")
    input_responsabil = input("Introdu persoana responsabila: ")
    input_asignare = input("Asigneaza tasku-l unei categorii: ")
    x = activitati.append(input_activitate)
    y = responsabil.append(input_responsabil)
    z = termen.append(input_termen)
    w = asignare.append(input_asignare)
    while input_asignare in categorie:
        return True
    else:
        print("Categoria introdusa nu se regaseste in cele declarate initial")
        input_asignare = input("Asigneaza tasku-l unei categorii: ")


def more_tasks():
    global input_activ
    more_task_to_input = input("Doresti sa continui cu introducerea de taskuri,' da / nu '")
    if more_task_to_input in ["da", "Da", "d", "D"]:
        return True
    elif more_task_to_input in ["nu", "No", "n", "N"]:
        input_activ = False
        return False


while input_activ is True:
    input_values()
    more_tasks()
with open("Categorii.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(categorie)
with open("Taskuri.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(activitati)
    csv_writer.writerow(responsabil)
    csv_writer.writerow(termen)
    csv_writer.writerow(asignare)


def printare_optiuni():
    print("1. Listare date")
    print("2. Sortare date:\n  2.1 Sortare ascendenta task\n  2.2 Sortare descendenta task")
    print("3. Filtrare date dupa: \n  3.1 Task: \n  3.2 Persoana resposabila\n  3.3 Deadline\n  3.4 Categorie")
    print("4. Adauga un nou task in lista : ")
    print("5.Sterge un task din lista")
    select_option = float(input("Pentru executarea unei actiuni listate de mai sus, introdu numarul aferent: "))
    if select_option in [1, 2, 2.1, 2.2, 3, 3.1, 3.2, 3.3, 3.4, 4, 5]:
        return True
    select_option = float(input("Pentru executarea unei actiuni listate de mai sus, introdu numarul aferent: "))


printare_optiuni()

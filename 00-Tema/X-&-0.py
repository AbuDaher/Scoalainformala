import random

utilizatori ={'Guest' : "X",
              'Computer' : "0"}
raspuns_utilizator = input("Vrei sa incepi tu jocul: 'da / nu' ? ")
raspuns_admis= ["da", "nu"]
if raspuns_utilizator in raspuns_admis:
    print("-----")
else:
    print("Raspunsul dat nu este admis, raspunde doar cu 'da' sau 'nu'")


pozitie = {  1  : "_",
             2  : "_",
             3  : "_",
             4  : "_",
             5  : "_", # prima completare
             6  : "_",
             7  : "_",
             8  : "_",
             9  : "_"}
def inceput_joc():
    if raspuns_utilizator == 'da':

        alegere_pozitie = input(f"{utilizatori['Guest']}, ai prima sansa la victorie, alege o cifra de la 1 la 9: ")

        pozitie[alegere_pozitie] = "x"
        print(pozitie)
        #
        # ramase =[1,3,5,7]
        # alegere_pozitie = random.choise(ramase)
        # pozitie[alegere_pozitie] = utilizatori['Computer']
        # print(pozitie)

    #
    # else:
    #     raspuns_utilizator == 'nu'
    #     print(f"{utilizatori['Computer']}, ai prima sansa la victorie, alege o cifra de la 1 la 9:")
    #     pozitie[5] = utilizatori['Computer']

inceput_joc()
# def runda_1():
#     while raspuns_utilizator == 'da':
#         alegere_pozitie = print(f"{utilizatori['Guest']}, alege inca o cifra de la 1 la 9: ")
#         if pozitie[1] == "_":
#             pozitie[1]= "x"
#             break
#         elif pozitie[3] == "_":
#             pozitie[3] = "x"
#             break
#         elif pozitie[7] == "_":
#             pozitie[7] ="x"
#             break
#         print(pozitie)
# #         else:
# #             alegere_pozitie = print(f"{utilizatori['Computer']},  alege inca o cifra de la 1 la 9: ")
# #             ramas = [1, 3, 5, 7]
# #             computer_choice = random.choice(ramas)
# #             while computer_choice  in ramas:
# #                 if pozitie[1] == "_":
# #                     pozitie[1] = "x"
# #                     break
# #                 elif pozitie[3] == "_":
# #                     pozitie[3] = "x"
# #                     break
# #                 elif pozitie[7] == "_":
# #                     pozitie[7] = "x"
# #                     break
# #                 print(pozitie)
# #     while raspuns_utilizator == 'nu':
# #         if pozitie[1] == "_":
# #             pozitie[1]= "x"
# #             break
# #         elif pozitie[3] == "_":
# #             pozitie[3] = "x"
# #             break
# #         elif pozitie[7] == "_":
# #             pozitie[7] ="x"
# #             break
# # print(pozitie)
# runda_1()
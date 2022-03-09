""" Se da urmatoarea lista:
lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’,
‘Claudiu’]
Se cere:
1. Sortati lista dupa nume
2. Determinati numarul de aparitii al fiecarui nume
3. Listati numele care apare de cele mai multe ori in lista initiala.
4. Listati numele care apare de cele mai putine ori in lista initiala.
Optimizati codul."""
#
# lista_nume = ["Maria", "Irina", "Claudiu", "Ionut", "Irina", "Matei", "Irina", "Maria", "Claudiu"]
#
#
# def sortare():
#     return sorted(lista_nume)
#
#
# print(sortare())
#
#
# def aparitii_nume():
#     setul_meu = set(lista_nume)
#     lista_unica = list(setul_meu)
#     lista_noua = []
#     for x in lista_unica:
#         y = lista_nume.count(x)
#         print(x, y)
#
#
# aparitii_nume()
#
#
# def min_max():
#     dictionarul_meu = {}
#     for i in lista_nume:
#         dictionarul_meu[i] = dictionarul_meu.get(i, 0) + 1
#     print(dictionarul_meu)
#     min_no = min(dictionarul_meu.values())
#     max_no = max(dictionarul_meu.values())
#     lista_min = []
#     lista_max = []
#     for i in dictionarul_meu:
#         if dictionarul_meu[i] == min_no:
#             lista_min.append(i)
#         if dictionarul_meu[i] == max_no:
#             lista_max.append(i)
#
#     print(lista_min)
#     print(lista_max)
#
#
# min_max()
'''
# 3. Sa se verifice daca doua stringuri sunt anagrame
# 4. Sa se elimine toate duplicatele dintr-o lista
5. Sa se verifice daca un string este palindrom
6. Sa se verifice ce numere lipsesc dintr-un interval
7. Sa se afiseze inversul unul string
8. Sa se afiseze toate permutarile dintr-un string'''


# def my_function(string1, string2):
#     message = ""
#     if sorted(string1) == sorted(string2):
#         message = "Sunt anagrame"
#         return message
#     return False
#
#
# print(my_function("maine", "imane"))



# def my_function():
#     lista = [1, 4, 3, 2, 3, 8, 1, 8, 9, 3]
#     my_set = set(lista)
#     lista = list(my_set)
#     return lista
#
#
# print(my_function())
#
#
# def duplicat(lista):
#     return list(dict.fromkeys(lista))
#
#
# print(duplicat([1, 4, 3, 2, 3, 8, 1, 8, 9, 3]))


# 5. Sa se verifice daca un string este palindrom

# def palindrom(expresie):
#     message = ""
#     if expresie[::-1] == expresie:
#
#         message = "Palindorm"
#         return message
#     return False
#
# print(palindrom("mamam"))

# sa se verifice ce numere lipsesc dintr-un interval:
#
# def functie(start: int, end: int):
#     lista = list(range(start, end+1))
#     interval = [1, 2, 3, 5, 6, 9, 10, 11]
#     lista_noua = []
#     for i in lista:
#         if i not in interval:
#             lista_noua.append(i)
#     return lista_noua
#
#
# print(functie(1, 12))


'''8. Sa se afiseze toate permutarile dintr-un string'''
"""Calculeaza n factorial"""
#
# def functia_mea(n):
#     if n == 1 :
#         return 1
#     return n * functia_mea(n-1)
#
#
# string = "123"
# n = len(string)
# new_list = []
# for c1 in range(0, n):
#     for c2 in range(0, n):
#         for c3 in range(0, n):
#             if c1 != c2 and c1 != c3 and c2 != c3:
#                 print(string[c1]+string[c2]+string[c3])
#
# functia_mea(n)
# #
# lista = ["apa", "sare", "cartofi", "paine", "sare"]
# lista_noua = [x if x != "sare" else "zahar" for x in lista]
# print(lista_noua)

string = "Ana are mere"
lista = [1, 2, 3, "a"]
for i, v in enumerate(lista):
        print(i,'=>',v)
for variabila_temporara in range(0,len(lista)):
         print(lista[variabila_temporara])
print(variabila_temporara,">>")













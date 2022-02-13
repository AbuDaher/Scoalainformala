# a = int(input("Scrie primul numar "))
# b = int(input("Scrie al 2-lea numar "))
# if a > b:
#     print("Primul numar este mai mare decat al 2-lea")
# elif a == b:
#     print("numerele sunt egale")
# else:
#     print("Al 2-lea numar este mai mare decat primul")
#
# a = int(input("Introdu un numar natural "))
# if a == 0:
#     b = int(input("b = "))
#     c = int(input("c = "))
#     print(int(b + c))
# else:
#     d = float(input("d = "))
#     e = float(input("e = "))
#     print(float(d * e))
#
# numar_analizat = int(input("Introdu un numar intreg "))
# if numar_analizat % 2 == 0:
#     print("numarul introdus este par")
# else:
#     print("numarul introdus este impar")
# print("Sfarsit")

# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# d = float(input("d = "))
# if c + d > 0:
#     print(float(a + b))
# elif c + d == 0:
#     print(float(a - b))
# else:
#     print(float(a * b))
# print("Sfarsit")

# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# p = 0
# if x % 2 == 0:
#     p += 1
# if y % 2 == 0:
#     p = p + 1
# if z % 2 == 0:
#     p = p + 1
# print("Numere pare sunt: ", p)

# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# d = 0
# if x % 3 == 0:
#     d = d + 1
# if y % 3 == 0:
#     d = d + 1
# if z % 3 == 0:
#     d = d + 1
# if d == 3:
#     print("Afirmatie punct 1 corecta")
# else:
#     print("Afirmatie punct 1 falsa")
# p = 0
# if x % 2 == 0:
#     p = p + 1
# if y % 2 == 0:
#     p = p + 1
# if z % 2 == 0:
#     p = p + 1
# if p == 2:
#     print("Afirmatie punct 2 corecta")
# else:
#     print("Afirmatie punct 2 falsa")
# c = 0
# # if x > 10:
# #     c = c + 1
# # if y > 10:
# #     c = c + 1
# # if z > 10:
# #     c = c + 1
# # if c == 3:
# if x > 10 and y > 10 and z > 10:
#     c = c + 1
#     print("Afirmatie punct 3 corecta")
# else:
#     print("Afirmatie punct 3 falsa")
#
# lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = int(input(" n= "))
# if n in lista1:
#     print("numarul se regasete in lista")
# else:
#     print("numarul nu se gaseste in lista")
#
#
# lista1 = ["a", "b", "c", "d", "e"]
# for x in lista1:
#     print(x)
# lista2 = [1, 2, 3]
# for x in lista2:
#     print(x)
# lista_3 = [1, 2, 3, 4, 5, 6]
# for x in lista_3:
#     if x % 2 == 0:
#         print(x)

# lista_1 = [1, 2, 3, 4, 5, 6]
# s1 = 0
# s2 = 0
# for x in lista_1:
#     if x % 2 != 0:
#
#         s1 = x + s1
# else:
#     for x in lista_1:
#         if x % 2 == 0:
#             s2 = x + s2
# print(s1,s2)
#
# dict1 = {1 : "a", 2 : "b", 3 : "c"}
# for x in dict1:
#     print(x)
#     print(dict1.get(x))


# n= int(input("introdu un numar natural: "))
# s = 0
# for x in range(n+1):
#     s = s + x
# print("Suma numerelor este",s)
#
# n = int(input("introdu un numar "))
# suma = 0
# i = 1
# while i <=n:
#     suma = suma + i
#     i = i + 1
# print("Suma este",suma)
#
# import random
# numar = random.randint(1,100)
# ghicit = int(input())
# while numar != ghicit:
#     if ghicit > numar:
#         print ("este maai mic")
#     else:
#         print("este mai mare")
#     ghicit = int(input())
# print("felicitari ai ghicit numarul")
#
# my_var = input("int number: ")
# try:
#     my_int = int(my_var)
# except ValueError as e:
#     print("Do something with Value error")
# else:
#     print("am ajuns aici pentru ca nu sunt exceptii")
# finally:
#     print("Am ajuns aici indiferent de exceptie")
#

# 2 Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n
#
#
# n = int(input("Introdu un numar natural: "))
# def sum_total(x):
#     s = 0
#     for i in range(x):
#          s += i + 1
#     return s
# print(su
#
# def suma_numere_pare(n):
#     if n <= 1:
#         return 0
#     if n == 2:
#         return n
#     if n == 3:
#         return n - 1
#     if n % 2 == 0:
#         return n + suma_numere_pare(n - 2)
#     else:
#         return n - 1 + suma_numere_pare(n - 2)
# print(suma_numere_pare(3))
# def suma_numere_impare(n):
#     if n <= 1:
#         return 0
#     if n == 1:
#         return n
#     if n == 2:
#         return n - 1
#     if n % 2 != 0:
#         return n + suma_numere_impare(n - 2)
#     else:
#         return n - 1 + suma_numere_impare(n - 2)
# print(suma_numere_impare(3))
#
# n = (input("Introdu un numar: "))
# def evaluare(n):
#     if n.isnumeric():
#         return n
#     else:
#         return print("Nu este un numar intreg")
#
# print(evaluare(n))

from datetime import date

def age(birthdate):
    today = date.today()
    age = today.year() - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
print(age(date(1988, 9, 19)))
# num_calls = 0
#
#
# def exercitiu(x):
#     global num_calls
#     num_cals = 3
#     num_calls += 1
#     return x * x
#
#
# print(exercitiu(4))
#
#
# x = 1
#
#
# def f():
#     return x
#
#
# print(x)
# print(f())
#
# x = (1, 2, 3)
#
# x[1] = 4
#
# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))
#
# a = [1, 2, 3]
# b = [4, 5]
# print(a + b*3)
#
# x = [1, 2, 3, 4]
# print(x[-1:])
#
# x = [0, 1, [2]]
# x[2][0]= 3
# x[2].append(4)
# x[2] = 2
# print(x)

#
# def exercitiu():
#     lista = [1, 2, 3]
#     for i in lista:
#         print(i)
#
#
# # x = exercitiu()
# print(exercitiu())
#
# a = range(10)
# y = [x * x for x in a if x % 2 == 0]
# print(y)
#
#
# def creare_lista():
#     n = int(input("introdu numarul de elem: "))
#     lista = []
#     for i in range(n):
#         element = input(f"elemenul {i} este : ")
#         lista.append(element)
#     return lista

# print(creare_lista())
# def afisare_lista(x):
#     for i in x:
#         print(i)
#
#
def functie():
    for i in range(10):
     print(i)
functie()

# lista1 = creareista()
# print(lista1)
# afisare_lista(lista1)


# def functie(x):
#     if -1 <= x >= 1:
#         x = (x + 1) / (1 + x * x)
#     elif -1 < x:
#         x = x + 1
#     x = 6 / (x + 1)
#     return x
# a = float(input("a = "))
# b = float(input("b = "))
# print("a este mai tare decat b") if a > b else print("b este mai mare decat a")
#
# print(functie(a))
# print(functie(b))
#

# lista1 = [1, 2, 3, [4, 5]]
# import copy
# lista2 = copy.copy(lista1)
# lista3 = copy.deepcopy(lista1)
# print(lista2)
# print(lista3)
# print(id(lista1), id(lista2), id(lista3))


# #
# def make_account():
#     return{"balance": 0}
#
#
# def deposit(account, amount):
#     account["balance"] += amount
#     return account["balance"]
#
# a = make_account()
# print(deposit(a, 10))

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#
# a = BankAccount()
# b = BankAccount()
# print(a.deposit(100))

# "foo" + 2

# try:
#     print("a")
# except ValueError:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

#
# print(list("python"))
# dict = {"x": 1, "y": 2}
# for i in dict:
#     print(dict[i])

# def funct(*args):
#     return 3 + len(args)
#
# print(funct(4, 4, 4))
#
# count = (3, 2, 5, 4)
# while len(count)<5:
#     count0 = count[0]+1
#     print("Hello Geek")
#

# def exercitiu(var):
#     for letter in "geeksforgeeks":
#         if letter == "e" or letter == "s":
#             continue
#         print("Current letter:", letter)
#         var = 10
#         return var
# print(exercitiu(20))

# def f(a, list=[]):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2,[1, 2, 3])
# f(2)


#
# list = ["1", "2", "3", "4", "5"]
# print(list[500:])











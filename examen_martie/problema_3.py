# Scrie un program care sa afiseze toate combinarile de 2 litere dintre valorile dictionarului de mai jos:

dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}
lenth = len(dictionar)


def my_function():
    lista= []
    for i in dictionar.values():
        lista.append(i)

    my_set = set(lista)

    lista= list(my_set)
    str = ""
    for i in lista:
        str = str + i
    print(str)
    n = len(str)
    for x in range(0,n):
        for y in range(0,n):
            print(str[x] + str[y])

my_function()

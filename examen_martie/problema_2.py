# 2. Scrie un program care sa elimine si sa printeze numerele din 3 in 3 pana cand lista devine goala. (1 punct)
# Lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def my_function():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    new_list = []
    for i in lista:
        if i % 3 == 0:
            lista.remove(i)
            print(lista)


my_function()

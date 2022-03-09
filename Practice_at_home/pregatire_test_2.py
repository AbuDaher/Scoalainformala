# 2. Se da urmatoarea lista:
# lista_nume = [‘Maria’, ‘Irina’, ‘Claudiu’, ‘Ionut’, ‘Irina’, ‘Matei’, ‘Irina’, ‘Maria’,
# ‘Claudiu’]
# Se cere:
# 1. Sortati lista dupa nume
# 2. Determinati numarul de aparitii al fiecarui nume
# 3. Listati numele care apare de cele mai multe ori in lista initiala.
# 4. Listati numele care apare de cele mai putine ori in lista initiala.
# Optimizati codul.

lista = ["Maria", "Irina", "Claudiu", "Ionut", "Irina", "Matei", "Irina", "Maria", "Claudiu"]


def sortare():
    lista.sort()
    return lista


print(sortare())


def aparitii():
    lista_unica = ["Maria", "Irina", "Claudiu", "Ionut", "Matei"]
    lista_aparitii= []
    for i in lista_unica:
        x = lista.count(i)
        print(f"Numele {i} apare de {lista.count(i)} ori ")
        lista_aparitii.append(x)
    dict = {}
    for n in lista_aparitii:
        for m in lista_unica:
            dict[n] = m
            lista_unica.remove(m)
            break
    a = dict.get(max(dict.keys()))
    b = dict.get(min(dict.keys()))
    print(f"Numele {a} apare de cele mai multe ori ,numele {b} pare de cele mai putine ori")

aparitii()


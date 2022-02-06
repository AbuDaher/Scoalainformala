print("Mesaj")
format()
a = input("input dat de utilizator")
def functia_mea():
    pass

# def functia_mea(param_1):
#     pass

def suma(a: int, b: int = 1, c: int=0) -> (int, int): # declaram parametri, daca declaram valori de aici ,
                                        # de unde incepem cu declararea trebuie sa declaram pana la ultimul parametru
    """                                          # asa se documenteaza functiile

    :param a: first param
    :param b: second param
    :param c: third param
    :return: sum of param
    """
    return a +b+c, a- b -c # de preferat sa folosim return in loc de print deoarece este posibil sa dea erori

variabila_1 = 1
variabila_2 = 2
sum, dif = suma(variabila_1, variabila_2) # parametri la apelare a functiei se numesc argumente
print(sum, dif)

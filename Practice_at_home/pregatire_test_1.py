# Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace
# battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.
#

# def conversie(str):
#
#     lista_string = list(str.split(" "))
#     return lista_string
#
#
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# a = conversie(string)
#
# def replacers(a):
#     patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
#     lista = [patches[0][2], patches[1][2], patches[2][2]]
#     a[1] = lista[0]
#     a[4] = lista[1]
#     a[8] = lista[2]
#     return a
#
#
# b = replacers(a)
#
#
# def reverse(b):
#     str1 = ""
#     for i in b:
#         str1 += i + " "
#     return str1
#
#
# print(reverse(b))


def nameChanger(x, y, z):
    string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
    start = string[5:14]
    end = string[26:31]
    text = string[43:49]
    string2 = string.replace(start, x)
    string3 = string.replace(end, y)
    string4 = string.replace(text, z)
    string_value = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
    lista = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
    for i in sorted(lista, reverse=True):
        # print(sorted(lista, reverse=True))
        string_value = string_value.replace(string_value[i[0]-1:i[1]], i[2])
        print(string_value, ">>>")


nameChanger("Conquistador", "King", "Palace")































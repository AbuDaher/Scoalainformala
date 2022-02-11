# 1 Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă
# numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
#
def suma_mea(*args):
    suma = 0
    for i in args:
     try:
        value = int(i)
        # print("Valuare nedefinita")
     except ValueError as e:
        # print("Exceptie intalnita Value")
        pass
     except TypeError as e:
         # print("Exceptie intalnita Type")
         pass
     else: suma = suma + value
     finally:
         print("Acest element a fost calculat")
    return suma
print(suma_mea(1, 5, -3, "abc", [12, 56, "cad"]))
print(suma_mea())
print(suma_mea(2, 4, "abc", "param1=2"))


# 2 Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
# ○ suma tuturor numerelor de la [0, n]
# ○ suma numerelor pare de la [0, n]
# ○ suma numerelor impare de la [0. n


def sum_total(x):
    s = 0
    for i in range(x):
         s += i + 1
    return s
print(sum_total(7))

def suma_p(n):
    if n <= 1:
        return 0
    if n == 2:
        return n
    if n == 3:
        return n - 1
    if n % 2 == 0:
        return n + suma_p(n - 2)
    else:
        return n - 1 + suma_p(n - 2)
print(suma_p(7))
def suma_i(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n % 2 != 0:
        return n + suma_i(n - 2)
    else:
        return n - 1 + suma_i(n - 2)
print(suma_i(7))

# 3. Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
# valoarea 0.

n = (input("Introdu un numar: "))

def evaluare(n):
    if n.isnumeric():
        return n
    else:
        return print("Nu este un numar intreg")

print(evaluare(n))

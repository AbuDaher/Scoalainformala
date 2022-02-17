# 1.


def suma_mea(*args):
    suma = 0
    for i in args:
        try:
            value = int(i)

        except ValueError:

            pass
        except TypeError:

            pass
        else:
            suma = suma + value
        finally:

            pass

    return suma


print(suma_mea(1, 5, -3, "abc", [12, 56, "cad"]))
print(suma_mea())
print(suma_mea(2, 4, "abc", "param1=2"))

# 2.


# def sum_t(x):
#     s = 0
#     for i in range(x):
#         s += i + 1
#     return s


# print(int(sum_t(7)))


def sum_t_i_p(x):
    s1, s2 = 0, 0

    for i in range(x):
        if i % 2 == 0:
            s1 = s1 + i + 1
        else:
            s2 = s2 + i + 1
    return print(f"Total {s1 + s2},Suma impar {s1}, Suma par {s2}")


sum_t_i_p(7)


# 3.

n = (input("Enter a number: "))


def evaluate():
    if n.isnumeric():
        return n
    else:
        return 0


print(evaluate())

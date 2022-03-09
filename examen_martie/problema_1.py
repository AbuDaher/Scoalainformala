# 1. Scrie un program care sa calculeze suma dintre trei numere. Daca valorile sunt egale, returnati de
# trei ori suma acestora.(1 punct)

def my_function(x:int,y:int,z:int):
    sum = 0
    if x == y and y ==z and x == z:
        sum = 3 * (x + y + z)
        return sum
    sum = x + y + z
    return sum


print(my_function(x=2, y=3, z=4))
print(my_function(x=5, y=5, z=5))
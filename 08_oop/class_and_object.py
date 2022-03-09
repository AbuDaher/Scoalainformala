# class MyFirstClass:
#
#     pass
#
# my_first_object = MyFirstClass()


class Caine:
    nr_picioare = 4  # acesta esrte un atribut

    def __init__(self, name, age):
        self.nume = name
        # self.varsta = age

    def __str__(self):
        self.nume = "Rex"

        return f"{self.nume}"

    def __change_name__(self, name):
        self.nume = name
# print(Caine.nr_picioare)

cainele_meu = Caine("Rex", "7")
# print(cainele_meu.nume)
print(cainele_meu.change_name("Ben"))
print(cainele_meu)
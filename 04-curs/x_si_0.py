import random

intrebare = input('Vrei sa incepi tu jocul? "y/n" ')

lista = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
if intrebare == 'y':
    valoare_utilizator = int(input("Zi-mi un numar de la 1 la 9! "))
    if lista[valoare_utilizator - 1] == "-":
        lista[valoare_utilizator - 1] = '[X]'

while "-" in lista:

    if lista[4] == "-":
        lista[4] = '[0]'
    elif lista[0] == "-":
        lista[0] = '[0]'
    elif lista[2] == "-":
        lista[2] = '[0]'
    elif lista[6] == "-":
        lista[6] = '[0]'
    elif lista[8] == "-":
        lista[8] = '[0]'
    else:
        ramas = [1, 3, 5, 7]
        computer_choice = random.choice(ramas)
        while computer_choice not in ramas:
            lista[computer_choice] = '[0]'

    # print(f"{lista[0]}   {lista[1]}   {lista[2]}\n"
    #       f"{lista[3]}   {lista[4]}   {lista[5]}\n"
    #       f"{lista[6]}   {lista[7]}   {lista[8]}")

    print("{}\t{}\t{} \n{}\t{}\t{}\n{}\t{}\t{}".
          format(lista[0], lista[1], lista[2], lista[3],
                 lista[4], lista[5], lista[6], lista[7], lista[8]))


    valoare_utilizator = int(input("Zi-mi un numar de la 1 la 9! "))
    if lista[valoare_utilizator - 1] == "-":
        lista[valoare_utilizator - 1] = '[X]'
    # print(lista)
    if lista[0] == lista[1] == lista[2] != "-":
        if lista[0] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[3] == lista[4] == lista[5] != "-":
        if lista[3] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[6] == lista[7] == lista[8] != "-":
        if lista[6] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[3] == lista[6] != "-":
        if lista[0] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[1] == lista[4] == lista[7] != "-":
        if lista[1] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[5] == lista[8] != "-":
        if lista[2] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[0] == lista[4] == lista[8] != "-":
        if lista[0] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')
    elif lista[2] == lista[4] == lista[6] != "-":
        if lista[2] == '[X]':
            print('Ai castigat!')
            break
        else:
            print('Ai pierdut!')

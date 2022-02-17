
print('Introdu CNP: ')
cnp =int(input())
print("-------------")
verificare_lg = str(cnp)
if len(verificare_lg) == 13:
    print("Ai respectat numarul recomandat de cifre")
    print("-------------")
else:
    print("Nu ai respectat numarul obligatoriu de cifre , asigura-te ca sunt 13")

def validare_gen():
    first_number = int(cnp / 1000000000000)

    feminin = [2, 4, 6]
    masculin = [1, 3, 5]
    f_rezident = [7]
    m_rezident = [8]
    straina = [9]
    if first_number in feminin:
        print("1. Persoana de gen feminin")
    elif first_number in masculin:
        print("1. Persoana de gen masculin")
    elif first_number in f_rezident:
        print("1. Persoana de gen feminin rezidenta in Romania")
    elif first_number in m_rezident:
        print("1. Persoana de gen masculin rezidenta in Romania")
    elif first_number == 9:
        print("1. Sunt persoana straina nerezidenta ")
    #return print
validare_gen()

def data_nastere():
    first_number = int(cnp / 1000000000000)
    categorie1 = [1, 2]
    categorie2 = [3, 4]
    categorie3 = [5, 6]
    categorie4 = [7, 8]
    categorie5 = [9]
    an_nastere = int((cnp / 10000000000) % 100)
    luna_nastere = int((cnp / 100000000) % 100)
    ziua_nastere = int(( cnp / 1000000) % 100)

    # print(an_nastere, luna_nastere, ziua_nastere)
    if first_number in categorie1:
        print(f"2. Te-ai nascut in anul 19{an_nastere} , in luna {luna_nastere}, in ziua {ziua_nastere}")
    elif first_number in categorie2:
        print(f"2. Te-ai nascut in anul 18{an_nastere} , in luna {luna_nastere}, in ziua {ziua_nastere}")
    elif first_number in categorie3:
        print(f"2. Te-ai nascut in anul 20{an_nastere} , in luna {luna_nastere}, in ziua {ziua_nastere}")
    elif first_number in categorie4:
        print(f"2. Rezident in Ro, te-ai nascut in anul 19{an_nastere} , in luna {luna_nastere}, in ziua {ziua_nastere}")
    else:
        print(f"2. Nerezident in Ro,te-ai nascut in anul 19{an_nastere}, in luna {luna_nastere}, in ziua {ziua_nastere}")
    return print

data_nastere()

from datetime import date, timedelta
def age():
    days_in_year = 365.2425
    today = date.today()
    categ_1 = [1, 2, 7, 8, 9]
    categ_2 = [5, 6]
    categ_3 = [3, 4]
    first_number = int(cnp / 1000000000000)
    an_nastere = int((cnp / 10000000000) % 100)
    luna_nastere = int((cnp / 100000000) % 100)
    ziua_nastere = int((cnp / 1000000) % 100)
    if first_number in categ_1:
        an_nastere = (1900 + an_nastere)
        age = (date.today() - date(an_nastere,luna_nastere,ziua_nastere)) // timedelta(days=365.2425)
        print(f"3. Esti in varsta de {age} ani")
    elif first_number in categ_2:
        an_nastere = (2000 + an_nastere)
        age = (date.today() - date(an_nastere, luna_nastere, ziua_nastere)) // timedelta(days=365.2425)
        print(f"3. Esti in varsta de {age} ani")
    else:
        an_nastere = (1800 + an_nastere)
        age = (date.today() - date(an_nastere, luna_nastere, ziua_nastere)) // timedelta(days=365.2425)
        print(f"3. Esti in varsta de {age} ani")
    return age
print(age)
age()

def judet():
    lista_judete ={
        0o1 : "Alba",
        0o2 : "Arad",
        0o3 : "Arges",
        0o4 : "Bacau",
        0o5 : "Bihor",
        0o6 : "Bistrita-Nasaud",
        0o7 : "Botosani",
        8   :  "Brasov",
        9   : "Braila",
        10 : "Buzau",
        11 : "Caras-Severin",
        12 : "Cluj",
        13 : "Constanta",
        14 : "Covasna",
        15 : "Dambovita",
        16 : "Dolj",
        17 : "Galati",
        18 : "Gorj",
        19 : "Harghita",
        20 : "Hunedoara",
        21 : "Ialomita",
        22 : "Iasi",
        23 : "Ilfov",
        24 : "Maramures",
        25 : "Mehedinnti",
        26 : "Mures",
        27 : "Neamt",
        28 : "Olt",
        29 : "Prahova",
        30 : "Satu Mare",
        31 : "Salaj",
        32 : "Sibiu",
        33 : "Suceava",
        34 : "Teleorman",
        35 : "Timis",
        36 : "Tulcea",
        37 : "Vaslui",
        38 : "Valcea",
        39 : "Vrancea",
        40 : "Bucuresti",
        41 : "Bucuresti S1",
        42 : "Bucuresti S2",
        43 : "Bucuresti S3",
        44 : "Bucuresti S4",
        45 : "Bucuresti S5",
        46 : "Bucuresti S6",
        51 : "Calarasi",
        52 : "Giurgiu",
    }
    judet_nastere = int(( cnp / 10000) % 100)
    corespondent = lista_judete.get(judet_nastere)

    if judet_nastere in lista_judete:
        print(f"4. Te-ai nascut in judetul {corespondent}")

    return print
judet()

def cifra_control():
    cifra =  int(( cnp % 10))
    calcul = ((int(cnp / 1000000000000)) * 2 + (int((cnp / 100000000000) % 10)) * 7 + (int((cnp / 10000000000) % 10)) * 9 + (int((cnp / 1000000000) % 10)) * 1 + (int((cnp / 100000000) % 10)) * 4 + (int((cnp / 10000000) % 10)) * 6 + (int((cnp / 1000000) % 10)) * 3 + (int((cnp / 100000) % 10)) * 5 + (int((cnp / 10000) % 10 )) * 8 + (int((cnp / 1000) % 10)) * 2 + (int((cnp / 100) % 10)) * 7 + (int((cnp / 10) % 10)) * 9) % 11
    if cifra == calcul:
        print (" Daca afirmatiile 1 + 2 + 3 + 4 sunt corecte, felicitari, CNP-ul tau este introdus corect")
    while calcul == 10:
        if cifra == 1:
            print ("Daca afirmatiile 1 + 2 + 3 + 4 sunt corecte, felicitari, CNP-ul tau este introdus corect")
        else:
            print("CNP-ul trebuie reintrodus, cifra de verificare nu este corecta ")

        break
cifra_control()
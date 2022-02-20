
input_user = input("Enter CNP: ")


def check_user_input():
    global input_user
    if len(input_user) != 13:
        try:
            input_user = input("Re-enter CNP ")
        except ValueError:
            input_user = input("Re-enter CNP ")
        finally:
            input_user = input("Re-enter CNP ")
    elif len(input_user) == 13:
        if input_user.isnumeric():
            input_user = int(input_user)
        else:
            input_user = input("Re-enter CNP ")
        return input_user


check_user_input()


def validate_gen():
    global input_user
    input_user = int(input_user)
    first_number = int(input_user / 1000000000000)
    female = [2, 4, 6]
    male = [1, 3, 5]
    f_resident = [7]
    m_resident = [8]
    if first_number in female:
        message1 = "1. Gender female"
    elif first_number in male:
        message1 = "1. Gender male"
    elif first_number in f_resident:
        message1 = "1. Female resident"
    elif first_number in m_resident:
        message1 = "1. Male resident"
    else:
        message1 = "1. Foreign "
    return message1


print(validate_gen())


def date_of_birth():
    global input_user
    input_user = int(input_user)
    first_number = int(input_user / 1000000000000)
    category1 = [1, 2]
    category2 = [3, 4]
    category3 = [5, 6]
    category4 = [7, 8]
    year_b = int((input_user / 10000000000) % 100)
    month_b = int((input_user / 100000000) % 100)
    day_b = int((input_user / 1000000) % 100)
    if first_number in category1:
        message = f"2. Born in 19{year_b} , month {month_b}, day {day_b}"
    elif first_number in category2:
        message = f"2. Born in 18{year_b} , month {month_b},day {day_b}"
    elif first_number in category3:
        message = f"2. Born in 20{year_b} , month {month_b}, day {day_b}"
    elif first_number in category4:
        message = f"2. Resident born in 19{year_b} , month {month_b}, day {day_b}"
    else:
        message = f"2. Foreign born in 19{year_b}, month {month_b}, day {day_b}"
    return message


print(date_of_birth())


from datetime import date, timedelta


def age():
    global input_user
    input_user = int(input_user)
    category1 = [1, 2, 7, 8, 9]
    category2 = [5, 6]
    first_number = int(input_user / 1000000000000)
    year_b = int((input_user / 10000000000) % 100)
    month_b = int((input_user / 100000000) % 100)
    day_b = int((input_user / 1000000) % 100)
    if first_number in category1:
        year_b = (1900 + year_b)
        your_age = (date.today() - date(year_b, month_b, day_b)) // timedelta(days=365.2425)
        message = f"3. Your age is: {your_age} years"
    elif first_number in category2:
        year_b = (2000 + year_b)
        your_age = (date.today() - date(year_b, month_b, day_b)) // timedelta(days=365.2425)
        message = f"3. Your age is: {your_age} years"
    else:
        year_b = (1800 + year_b)
        your_age = (date.today() - date(year_b, month_b, day_b)) // timedelta(days=365.2425)
        message = f"3. Your age is: {your_age} years "
    return message


print(age())


def land():
    message = ''
    global input_user
    input_user = int(input_user)
    list_lands = {
        0o1: "Alba",
        0o2: "Arad",
        0o3: "Arges",
        0o4: "Bacau",
        0o5: "Bihor",
        0o6: "Bistrita-Nasaud",
        0o7: "Botosani",
        8:  "Brasov",
        9: "Braila",
        10: "Buzau",
        11: "Caras-Severin",
        12: 'Cluj',
        13: "Constanta",
        14: "Covasna",
        15: "Dambovita",
        16: "Dolj",
        17: "Galati",
        18: "Gorj",
        19: "Harghita",
        20: "Hunedoara",
        21: "Ialomita",
        22: "Iasi",
        23: "Ilfov",
        24: "Maramures",
        25: "Mehedinnti",
        26: "Mures",
        27: "Neamt",
        28: "Olt",
        29: "Prahova",
        30: "Satu Mare",
        31: "Salaj",
        32: "Sibiu",
        33: "Suceava",
        34: "Teleorman",
        35: "Timis",
        36: "Tulcea",
        37: "Vaslui",
        38: "Valcea",
        39: "Vrancea",
        40: "Bucuresti",
        41: "Bucuresti S1",
        42: "Bucuresti S2",
        43: "Bucuresti S3",
        44: "Bucuresti S4",
        45: "Bucuresti S5",
        46: "Bucuresti S6",
        51: "Calarasi",
        52: "Giurgiu",
    }
    land_birth = int((input_user / 10000) % 100)
    corespondent = list_lands.get(land_birth)
    if land_birth in list_lands:
        message = f"4. You are born in {corespondent}"
    return message


print(land())


def control():
    message = ''
    global input_user
    input_user = int(input_user)
    digit = int((input_user % 10))
    check = ((int(input_user / 1000000000000)) * 2 + (int((input_user / 100000000000) % 10)) * 7
             + (int((input_user / 10000000000) % 10)) * 9 + (int((input_user / 1000000000) % 10)) * 1
             + (int((input_user / 100000000) % 10)) * 4 + (int((input_user / 10000000) % 10)) * 6
             + (int((input_user / 1000000) % 10)) * 3 + (int((input_user / 100000) % 10)) * 5
             + (int((input_user / 10000) % 10 )) * 8 + (int((input_user / 1000) % 10)) * 2
             + (int((input_user / 100) % 10)) * 7 + (int((input_user / 10) % 10)) * 9) % 11
    if digit == check:
        message = "CNP valid"
    elif check == 10:
        if check // 10 == 1:
            message ="CNP valid"
    else:
        message = "CNP invalid"
    return message


print(control())

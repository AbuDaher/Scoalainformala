# Creati un program in care utilizatorul sa introduca o adresa de email de formatul litere_sau_cifre@litere_sau_cifre.litere.
# Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa exista o singura
# data in sirul de caractere

email = input("introdu adresa de email: ")
import re
regex = "[a-z0-9]+[@]?\w+[.]?\w+{2,3}$"

def check(email):
    if  re.fullmatch(regex, email):
        print("Email-ul este invalid")
    else:
        print("Email-ul este valid")
    return email
    email = "andreea2324@gmail.com"
    print(check(email))




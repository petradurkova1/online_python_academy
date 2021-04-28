# 1. Vyžádá si od uživatele přihlašovací jméno a heslo.
USER = input('username: ')
PASSWORD = input('password: ')

# Registrováni jsou následující uživatelé:
USER_PASSWORD = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
ODDELOVAC = "-" * 40
# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
# 3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program.
if USER in USER_PASSWORD and USER_PASSWORD [USER]==PASSWORD:
    print("Welcome to the app, " + USER + ". We have 3 texts to be analyzed.")
else:
    print("Your name or your password is not registered. The program will quit")
    quit()
print(ODDELOVAC)

# 4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

selection = int(input("Enter a number btw. 1 and 3 to select:"))
if not (selection >= 1 and selection <=3):
    print("Selected text not in the offer. The program will quit")
    quit ()
print(ODDELOVAC)

# 5. Pro vybraný text spočítá následující statistiky:
#počet slov,
sekce = TEXTS[selection-1]
slova = sekce.split()
print ("There are " ,len(slova), " words in the selected text.")

#počet slov začínajících velkým písmenem,
pocet_slov_zacinajici_velkym_pismenem = 0
for slovo in slova:
    if slovo[0].isupper():
        pocet_slov_zacinajici_velkym_pismenem = pocet_slov_zacinajici_velkym_pismenem + 1
print ("There are " ,pocet_slov_zacinajici_velkym_pismenem, " titlecase words.")

#počet slov psaných velkými písmeny,
pocet_slov_psanych_velkym_pismenem = 0
for slovo in slova:
    if slovo.isupper() and slovo.isalpha():
        pocet_slov_psanych_velkym_pismenem = pocet_slov_psanych_velkym_pismenem + 1
print ("There are " ,pocet_slov_psanych_velkym_pismenem, " uppercase words.")

#počet slov psaných malými písmeny,
pocet_slov_psanych_malymi_pismenem = 0
for slovo in slova:
    if slovo.islower():
        pocet_slov_psanych_malymi_pismenem = pocet_slov_psanych_malymi_pismenem + 1
print ("There are " ,pocet_slov_psanych_malymi_pismenem, " lowercase words.")

#počet čísel (ne cifer),
pocet_cisel = 0
for slovo in slova:
    if slovo.isnumeric():
        pocet_cisel = pocet_cisel + 1
print ("There are " ,pocet_cisel, " numeric strings.")

#sumu všech čísel (ne cifer) v textu.
soucet_cisel = 0
for slovo in slova:
    if slovo.isnumeric():
      soucet_cisel = soucet_cisel + int(slovo)
print ("The sum of all the numbers" ,soucet_cisel, ".")

#Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu:

# vypocet nejdelsiho slova v textu bez interpunkce
nejdelsi_slovo = 0
for slovo in slova:
    if nejdelsi_slovo < len(slovo.strip(",.:;'")):
        nejdelsi_slovo = len(slovo.strip(",.:;'"))

# vytvoreni seznamu Occurences. Occurences je pocet slov s konkretni delkou.
max_pocet_slov = 0
SEZNAM = list()
for delka_slova in range(1, nejdelsi_slovo):

    OCCURENCES = 0
    for slovo in slova:
        if len(slovo.strip(",.:;'")) == delka_slova:
            OCCURENCES = OCCURENCES + 1
        if max_pocet_slov < OCCURENCES:
            max_pocet_slov = OCCURENCES
    SEZNAM.append(OCCURENCES)

if max_pocet_slov < 12:
    MEZERA = ""
else:
    MEZERA = " " * (max_pocet_slov - 12)
print (ODDELOVAC)
print ("", "LEN|  OCCURENCES ",MEZERA,"|NR.")
print (ODDELOVAC)

# Vypsani seznamu Occurences
for delka_slova in range (1, nejdelsi_slovo):
    HVEZDICKY = "*" * SEZNAM[delka_slova - 1]
    MEZERA = " " * (max_pocet_slov - SEZNAM[delka_slova - 1])
    if delka_slova < 10:
        print (" ",delka_slova, "|" ,HVEZDICKY, MEZERA,"|" ,SEZNAM[delka_slova - 1])
    else:
        print ("",delka_slova, "|" ,HVEZDICKY, MEZERA,"|" ,SEZNAM[delka_slova - 1])










#Podmínky v Pythonu umožňují provádět různé akce na základě splnění určitých kritérií. Klíčová slova if, elif a else se používají k definici podmínek.

# ----------------------------------------------------------------------
# if podmínka1:
    # provedený kód, pokud je podmínka1 splněna
# elif podmínka2:
    # provedený kód, pokud je podmínka2 splněna a podmínka1 není splněna
# else:
    # provedený kód, pokud žádná předchozí podmínka není splněna
# ----------------------------------------------------------------------


# Podmínky
    # == --> Rovnost
    # < , > --> Menší než, větší než
    # <= , >= --> Menší nebo rovná se , větší nebo rovná se
    # podminka1 and podminka2 --> and --> Jestliže podminka1 a podminka2 bude True provede se blok kodu, zdali obě nebo jedna bude False blok kodu neproběhne
    # podminka1 or podminka2 --> or --> Musí být alespoň jedna podmínka True aby proběhl blok kodu
    # hodnota in seznam --> in --> Zkontrluje zdali se hodnota nacházi v senzamu
    # isinstance (proměnná, datový typ) --> Kontorulje datový typ
    # ! nebo not - Negace hodnotu
    # x != y - Pokud se nerovná v podmínce

# Příklady

# Vyhodnocení znaku čísla
cislo = 15
print("Velikost čísla")
print(" Váše číslo =", cislo)


# Podmínky píšeme takto, vždy ukončíme ":"
# Pozor na syntaxi jazyka, zde se odsazuje, pokud bloku kodu spada pod podmínku, která se má vykonat.
# Odsazujeme tlačítkem TAB
# Pokud by blok jazyka nebyl odsazený, je možné, že bude hlásit chybu či se dokonce blok kódu vykoná jinak, než jste chtěli 
if cislo == 0:
    print(" Číslo je 0") # Všimnite si jak je blok kodu v if odsazený, tímto říkáme pythonu, že se má za splněných podmínek splnit tato část kódu
elif cislo < 0: # Pokud nebude platit předchozí podmínka, porovnává další podmínku
    print(" Číslo je větší než 0") # Pokud byla splněná první podmínka, tato podmínka neproběhná a python celou podmínku dále nečte
else: # Vykoná se pokaždé, pokud podmínky nebyly splněny
    print(" Číslo je číslo je menší než 0")







# Kontrola datového typu
print("Kontrola datového typu")
x = 10
print(" Hodnota x =", x)

if isinstance(x, int): # do závorek píšeme parametry funkce isinstance
    print(" Hodnota x je celé číslo")
elif isinstance(x, float):
    print(" Hodnota x je desetinné číslo")
else:
    print(" Hodnota x není číslo")



# Kontrola vstupu od uživatele
print("Kontrola zadané honodty")
prezdivka = input(" Zadej své jméno: ")

if prezdivka: # Pokud uživatel zadal nějakou hodnotu, splní se tak podmínka
    print(" Vítej,", prezdivka)
else: # Jestliže užvatel nezadal žádnou hodnotu
    print(" Nezadal jsi žádnou prezdivku")


# Výpis do příkazového řádku
# díky funkci print() mužeme vypisovta hodnoty v kulatých závorkách do příkazového řádku)

# ---------------------------------------------------------
# print(Hotnota kterou checeme vypsat do příkazového řádku)
# ---------------------------------------------------------

print("Hello world!") # Výstup Hello world!

# Vytvoření proměnných s různými datovými typy

# -----------------------------------
# název_proměnné = hodnota v promenné ## Vyhněte se diakritice v názvech proměných ##
# -----------------------------------

print(" ")

# Příklady datových typů v proměnných. Této operace se říká přesně inicializace proměné.
# Můžete se setkat i s výrazem deklarace. Obě varianty jsou v pořádků.
# ----------------------------------------------------------------------------------------------------------
# Pro lepší pochopení: 
#       Deklarace - Říkáme, že proměná existuje, ale nemá žádnout hodnotu, též musí mít přiřazený datový typ
#       Inicializace - Přiřazení hodnoty k proměnný.
# ----------------------------------------------------------------------------------------------------------

a = int; #Zde se jedná o deklaraci proměné bez hodnoty, protože jsme jí neinicializovali hodnotu

# Příklady inicializace proměných s jejich datovými typy
vek = 25           # typ int
jmeno = "Václav"   # typ str
je_muz = True      # typ bool
je_muz0 = 0        # typ bool v číselné hodnotě False
je_muz1 = 1        # typ bool v číselné hodnotě True
vyska = 175.5      # typ float

# Datové Typy
# -----------
#   Integers (celá čísla): Reprezentují celé číselné hodnoty, například věk.
#   Strings (řetězce): Reprezentují textové hodnoty, například jméno.
#   Booleans (logické hodnoty): Reprezentují logické hodnoty True (pravda) nebo False (nepravda).
#   Floats (desetinná čísla): Reprezentují desetinné číselné hodnoty, například výšku.


# Ukázka výpisu hodnot proměnných
print("Osobní údaje:") # Do samostatných printu můžeme takto psát jen jeden datový typ
print(" Věk:", vek) # Pokud chceme spojit například string a integers, odělujeme je čárkou
print(" Jméno:", jmeno)
print(" Je muž:", je_muz)

# F-string
print(f" Výška: {vyska}")
#     ↑        ↑     ↑ 
#     |       Do složených závorek napíšeme proměnnou, která nám umožní vypsat do printu i jiné datové typy.
#     |
# Píšeme f před uvozovky
# Výhoda v čitelnosti kódů
# V pythonu mužeme provádět zkoušky , díky kterým se mužeme vyhnout přerušení kódu kvůli erroru
# Zkoušku porvadíme pomocí 'try' a 'except'

#----------------------------------------------------------------------------------------------
#try:
#    zde dáme blok kodu pro zkoušku
#except Zde dáme typ erroru:
    # Jestliže se vyskytne v bloku kodu v try error, tak blok kodu přeskoči a sputstí se tento
#finally:
    # Blok kodu vždy proběhne
#----------------------------------------------------------------------------------------------

x = "1"
y = 2

print("Kod s errorem")
# Kod s errorem
try:
    z = x + y  #TypeError: chyba datového typu, nemužem sčítat intiger a string
    print(" Zde není žádná chyba, výsledke je", z)
    # Tento blok kodu neprobehne z duvodu erroru
except TypeError:
    print(" V kodu nastala chyba")
finally:
    print(" Proběhla zkouška")

print("Kod bez erroru")
# Kod bez erroru
try:
    z = int(x) + y  #Výstup: 3
    print(" Zde není žádná chyba, výsledke je", z)
    # V kodu nenastala chyba kod v pořádku porběne
except TypeError:
    print(" V kodu nastala chyba")
    # Tento blok kodu neprobehe, jelikož nenastala chyba
finally:
    print(" Proběhla zkouška")
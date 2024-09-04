# Funkce jsou bloky kódu, které provádějí určité operace a mohou být znovu použity.

#-----------------------------------------------------------------
# def add(Zde dáme parametry funkce):
#    Zde zadame kod který cheme mít ve funkci
#    return  To co dáme do return tak bude mít hodnotu ve funkci
# ----------------------------------------------------------------

# Jestliže máme ve funkci více return, a jedna z nich bude zaktivovaná tak se funkce ukončí a dašlí kody budou přeskočeny
# Vyvolání funkce
# add(zde dáme hodnoty pro paramtery) 

# Vytvoření funkce
# Def - definice funkce, klíčové slovo pro vytvoření funkce
# soucet - název funkce
# soucet(x,y) - parametry funkce, které využíváme ve funkci a které pak při volání uživatel zadávají
def soucet(x, y): 
  z = x + y
  return z   # Vrátí výsledek, respektive při volání se funkce provede vypíše se místo ní výsledek z return

cislo1 = 3
cislo2 = 4

# Vyvolání funkce
vysledek = soucet(cislo1, cislo2)
# cislo1 a cislo2 ted budoud ve funkci změněny na x a y
# Je to pododbné jako překopírovvání porměnné
# x = cislo1 a y = cislo2
# V jakém pořadí porměnné napíšeme, tak takový parametr dostane hodnotu

# Výpis výsledku
print("Výsledek sčítání je:", vysledek)  # Očekávaný výstup: 7




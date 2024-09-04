# While cyklus provádí blok kódu opakovaně, dokud je podmínka pravdivá.

# -------------------------------------------------------------
# While loop pdomínka 
    # While bude porbíhat do té doby dokud nebude podmínka False 
# --------------------------------------------------------------




print("Cyklus while:")

# Vytvoření proměnné řady
rada = 1

# While bude porbíhad do té doby, dokud nebude podmínka False
while rada < 6:
    print(" Na řadě je hráč s číselm:", rada)
    rada += 1

# Všimněte si, že pomocí While lze takto i udělat cyklus s pevným počtém opakováním
# Může za to inicializace proměné "rada = 1", tím jsme mu dali začátek cyklu a v podmínce porovnáváme zda rada je menší než 6
# Pokažde pak na konci cyklu přičítáme 1 do proměné rada a cyklus se opakuje odzačátku
# Pokud podmínka ve while bude False (nebude splněná podmínka), blok kódu ve While se již neprovede a pokračuje dal


# For loop cyklus
# -----------------------------------------------------------------------
# for i in range()
    # i --> v i máme začátek cyklu (defualtně je od 0)
    # range(počet trvání cyklu) --> díky funkci range zadáme kolikrát bude cyklus for porbíhat
# ------------------------------------------------------------------------


print("Cyklus for:")
print(" Čísla od 0 do 5:")

# For proběhne 6 krát
for i in range(6):
    print(" Číslo na řadě:", i) # Všimněte si, že i se takto dá využít pro vypis cyklu

# Práce s forem je komplexnější a nabízí výbornou práci s polem a objektama
# Inicializace i ve for hned po dokončení cyklu zaniká a lze jí používat v jiných cyklech

#Lze nastavit i od kud má i začít
for i in range(3, 6):  # Začínáme od 3 a jdeme do 5
    print("Číslo na řadě od 3:", i)

# Pro seznamy, které mají začínat od 1
for i in range(6): 
    print(i + 1, "Pořadí") # Díky tomu, že v cyklu vždy přidáváme 1, tak se nám bude vypisovat i od 1 
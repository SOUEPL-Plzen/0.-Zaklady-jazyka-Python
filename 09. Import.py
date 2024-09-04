# Import slouží k imporotvání ruzých modulu, díky kterým získáme spoustu novích funkcí

# -------------------
# import nazve_modulu
# -------------------

# Import modulu random pro použití funkcí náhodné generace
import random

# Použití funkce randint pro generování náhodných celých čísel
vyherni_cislo = random.randint(1,10) # volám knihovnu random ## randint - funkce v knihovně, kterou cheme použít, funkce slouží jako "Vygeneruj celá čáslo(od, do)"


print("Vyherní čislo je:", vyherni_cislo)  # Výstup: čílso od 1 do 10

# Je sposuta modulů se kterýma lze v pyhotnu pracovat , jako např. 
# pygame - pro vývoj her
# time - pracování s časem (pozastavit kod, hodin atd.) 
# os - práce se soubory
# a mnoho dlaších

# Některé knihovny musíte instalovat pomocí terminálů nebo lokálního importu
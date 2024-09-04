# Přetipování umožňuje konverzi proměnné na jiný požadovaný datový typ.
# Pomocí přetipování můžete konvertovat vstup do různých datových typů, například na celé číslo (Integer).

# ---------------------------------------------------
# str/int/float/bool(zde dáme proměnná kterou cheme přetipovat)
# ---------------------------------------------------

x = "1"
y =  2
x = int(x) # x - Změní z datového typu string na integer, této operace se říká PŘETYPOVÁNÍ.
z = x + y
print("Sčítání:", z)  # Výstup: 3

# Pozor!
x = str(x) # x - Změní z datového typus integer na string, této operace se říká PŘETYPOVÁNÍ.
a = "6"

# Výsledek se řetězí vedle sebe jako znaky
vysledek = x + a # Zde sčítáme stringy dohromady a výsledek nebude 3, ale 16!

# str() - přetipování na string
# int() - přetipování na intiger
# bool() - přetipování na bolleans
# float() - přetipování na float

# Získání vstupu od uživatele jako desetinné číslo
vstup = float(input("Zadej desetinné číslo: ")) # Probíhá ihned přetypování ve vstupu.
print("Zadali jste číslo:", vstup)

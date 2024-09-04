# S porměnnýma mužeme různě pracovat, ale dejte si pozor na datové typy, 
# Nemůžete například pracovat se Stringem a Integrem společně v printu. 

# Oproti tomu Float a Integer mužete spojovta dohomrady, jelikož jsou datové typ s číslicí, 
# V takovém případě bude výsledek pokaždé Float, pokud nepřetypujete výsledek jinak

# Vytvoření proměnných
x = 5
y = 3
pismeno1 = "A"
pismeno2 = "B"

# Sčítání
z = x + y
slovo = pismeno1 + pismeno2
print("Sčítání:", z)  # Výstup: 8
print("Sčítání string:", slovo) # Výstup: AB

# Odčítání
z = x - y
print("Odčítání:", z)  # Výstup: 2

# Násobení
z = x * y
slovo = pismeno1 * 5
print("Násobení:", z)  # Výstup: 15
print("Násobeni string:", slovo ) # Výstup: AAAAA 

# Dělení
z = x / y
print("Dělení:", z)  # Výstup: 1.6666666666666667

# Umocnění
z = x ** y
print("Umocnění:", z)  # Výstup: 125

# Možnosti s proměnnými
# Proměnné mohou být přiřazeny hodnoty z jiné proměné nebo mohou být použity k ukládání různých hodnot.

# Změna hodnoty proměnné
x = 5
x = 10
print("Hodnota proměnné x je:", x)  # Výstup: 10

# Priřazená hodnota z jiné hodnoty proměnné
x = 10
y = x
print("Hodnota proměnné y je:", y)  # Výstup: 10
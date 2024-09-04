# Slovník je datová struktura , ve které se nachází klíče
# Do každého klíče mužeme dávat jakoukoliv hodntou s ruznými datovími typy
# Slovník vyrtváříme pomocí {}, klíče jsou vetšinou vytvořeny v datovém typu string/intiger
# Pro založení dalšího kliče používáme čárku

# -------------------------------------------------
# nazev_slovniku = {
    # nazve_klice: hodnota_klice,
# }
# -------------------------------------------------

# Založení slovníku
klient = {
    "jméno": "Pavel",
    "přijmení": "Novák",
    "věk": 25,
}

# Výpis slovníku
print("Jméno klienta: ", klient["jméno"]) # Výpis: ... Pavel

# Smazání v slovníku 
klient.pop("přijmení") # Smaže se ze slovníku

# Přidání do slovníky
# nazev_slovniku[nazev_klice] = hodnta_klice
klient["přijmení"] = "Novotný"
print("Přijmení klienta: ", klient["přijmení"]) # Výpis: ... Novotný


# Změna hodnty v klíči
klient["věk"] = 26
print("Věk klienta: ", klient["věk"]) # Výpis: ... 26


# Podrobněji:

# Vytvoření seznamu klientů, kde každý klient je reprezentován slovníkem
# Vytvoření seznamu klientů, kde každý klient je reprezentován slovníkem (nikoli přímo objektem).
# Objekt zde může být závadějicí

# Slovník můžeme brát jako "objekt", který má svoje "vlastnosti" přesněji klíč
klienti = [
    {   # Slovník na pozici 0
        "jméno": "Pavel",      # Klíč "jméno" a jeho hodnota "Pavel"
        "příjmení": "Novák",   # Klíč "příjmení" a jeho hodnota "Novák"
        "věk": 25,             # Klíč "věk" a jeho hodnota 25
        "město": "Praha"       # Klíč "město" a jeho hodnota "Praha"
    },
    {   # Slovník na pozici 1
        "jméno": "Jana",
        "příjmení": "Dvořáková",
        "věk": 30,
        "město": "Brno"
    },
    {   # Slovník na pozici 2
        "jméno": "Karel",
        "příjmení": "Svoboda",
        "věk": 28,
        "město": "Ostrava"
    }
]

# Seznam obsahuje 3 slovníky, proto délka seznamu je 3.

# Výpis informací o každém klientovi v seznamu
for klient in klienti:
    # Přístup ke klíčům "jméno", "příjmení", "věk" a "město" v každém slovníku
    print(f"Jméno: {klient['jméno']}, Příjmení: {klient['příjmení']}, Věk: {klient['věk']}, Město: {klient['město']}")




# Pomocí pythonu mužeme číst nebo vytvářet soubory

# -----------------------------------------------
   # with open("nazev_souboru.txt","prace_se_souborem") as nazev_promenne

    # Možnosti pracovat se souborem:
        # r = přečtení souboru
        # w = vytvoření soubour

    # Funkce:
        # .read() = funkce na přeštení kodu
        # .write() = Do závorek dáme to co cheme vypsat do souboru
# ------------------------------------------------
#!!!! NEZAPOMEŇTE ŽE SOUBOR MUSÍ BÝT VE STEJNÉ SLOŽCE, JINKA MUSÍŠ ZKOPÍROVAT JEHO CESTU V ULOŽISTI NEBO NASTANE CHYBA!!!!


# Vytvoření a otevření souboru v režimu zápisu
with open("novy_soubor.txt", "w") as vy_soubor:
    # Zápis textu do souboru
    vy_soubor.write("Tohle je muj soubor vytvoření v pythonu")


# Otevřeme soubor pro čtení
with open("novy_soubor.txt", "r") as pre_soubor:
    # Přečteme celý obsah souboru
    obsah = pre_soubor.read()
    print("Obsah souboru je:")
    print(obsah)

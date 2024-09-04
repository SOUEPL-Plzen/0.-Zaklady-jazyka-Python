# Třídy využíváme k tomu, abychom vytvořili vlastní knihovnu funkcí a objektů

# Třídy jsou základním stavebním kamenem objektově orientovaného programování (OOP) v Pythonu. 
# Pomocí tříd můžeme definovat šablony (vzory) pro vytváření objektů. 
# Každý objekt má své vlastnosti a metody, které definují, co objekt může dělat a jak se může chovat.

# Třída se definuje pomocí klíčového slova `class`:
#---------------------------------------------
# class NazevTridy:
#     # Zde vytvoříme metody (funkce) a atributy (proměnné)
#---------------------------------------------

# Vytvoření instance třídy a volání metod:
# instance = NazevTridy()
# instance.nazevMetody(parametry)

# ---------------------------------------------
# Ukážeme si příklad, ve kterém vytvoříme kalkulačku pro sčítání a odčítání:

# Vytvoření třídy
class Kalkulacka:
    # Vytvoření metody pro sčítání
    def scitani(self, cislo1, cislo2):
        vysledek = cislo1 + cislo2
        return vysledek
    
    # Vytvoření metody pro odečítání
    def odecitani(self, cislo1, cislo2):
        vysledek = cislo1 - cislo2
        return vysledek

# Vytvoření instance třídy
kalkulacka = Kalkulacka()

x = 5
y = 6

# Vyvolání metody pro sčítání
vysledek1 = kalkulacka.scitani(x, y)

# Vyvolání metody pro odečítání
vysledek2 = kalkulacka.odecitani(x, y)
print("Kalkulačka")
print(" Sečtení čísel:", vysledek1)
print(" Odečtení čísel:", vysledek2)

# Dědičnost
# Mezi třídami můžeme dědit, například parametry, či metody

class DomaciMazlicek:
    # Pomocí metody __init__ můžeme inicializovat atributy
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def pohyb(self):
        print(f" {self.jmeno} se pohybuje.")

# Třída, která dědí z DomaciMazlicek
class Pes(DomaciMazlicek):
    def zvuk(self):
        print(f" {self.jmeno} štěká.")

# Použití dědičnosti
print("Domácí zvíře")
pes = Pes("Rex")
pes.pohyb()  # Výstup: Rex se pohybuje.
pes.zvuk()   # Výstup: Rex štěká.

# Podrobněji: 

# Definice třídy Auto
# Třída Auto je šablona pro vytváření objektů, které představují auta.
class Auto:
    # Konstruktor (__init__) se volá automaticky při vytváření nové instance (objektu) třídy.
    def __init__(self, znacka, barva):
        # Atributy "znacka" a "barva" se přiřadí k objektu pomocí klíčového slova self.
        # Self znamená, že tyto atributy patří konkrétnímu objektu, který se vytváří.
        self.znacka = znacka
        self.barva = barva

    # Definice metody popis, která vypíše informace o autu.
    # Metody jsou funkce, které provádí nějaké akce s objektem.
    def popis(self):
        print(f"Auto značky {self.znacka} má barvu {self.barva}.")

# Vytvoření nové instance třídy Auto (konkrétního objektu)
# Tímto voláme konstruktor __init__, který inicializuje hodnoty atributů "znacka" a "barva".
moje_auto = Auto("Škoda", "červená")

# Další instance třídy Auto
tvoje_auto = Auto("BMW", "modrá")

# Zavolání metody popis pro každou instanci
# Zde se použije metoda popis k zobrazení informací o každém autě.
moje_auto.popis()  # Výstup: Auto značky Škoda má barvu červená.
tvoje_auto.popis()  # Výstup: Auto značky BMW má barvu modrá.


# DĚDIČNOST
# Dědičnost je způsob, jakým jedna třída (podtřída) může zdědit vlastnosti a metody jiné třídy (rodičovské třídy).
# Vytvoříme podtřídu, která dědí z třídy Auto.

# Definice nové třídy SportovniAuto, která dědí (extends) z třídy Auto.
class SportovniAuto(Auto): # Do parametru zapisujeme jakou třídu chceme dědit
    # Konstruktor podtřídy, který volá konstruktor rodičovské třídy pomocí super()
    # a navíc přidává nový atribut "max_rychlost".
    def __init__(self, znacka, barva, max_rychlost):
        # Volání rodičovského konstruktoru pomocí super().
        # Tímto nastavujeme "znacka" a "barva" stejně jako v třída Auto.
        super().__init__(znacka, barva)
        # Přidání nového atributu "max_rychlost", který je specifický pro Sportovní auta.
        self.max_rychlost = max_rychlost

    # Nová metoda specifická pro SportovniAuto
    # Přidává informace o maximální rychlosti.
    def popis_sportovniho_auta(self):
        print(f"Sportovní auto značky {self.znacka} má barvu {self.barva} a maximální rychlost {self.max_rychlost} km/h.")

# Vytvoření instance třídy SportovniAuto
moje_sportovni_auto = SportovniAuto("Ferrari", "černá", 350)

# Použití metody z rodičovské třídy
moje_sportovni_auto.popis()  # Výstup: Auto značky Ferrari má barvu černá.

# Použití metody specifické pro podtřídu
moje_sportovni_auto.popis_sportovniho_auta()  # Výstup: Sportovní auto značky Ferrari má barvu černá a maximální rychlost 350 km/h.

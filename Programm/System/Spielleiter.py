from .Spieler import Spieler

class Spielleiter:
    def __init__(self):
        self.setUp()

    def setUp(self):
        print("Willkommen zu Monopoly im Terminal. \n "
              "Dieses Spiel können 2-4 Spieler mit einer Tastatur spielen. \n")
        anzahl = input("Wie viele Spieler werden spielen?\n")
        while int(anzahl) > 4 or int(anzahl) < 2:
            anzahl = input("Die Spielerzahl muss zwischen 2 und vier liegen, bitte nocheinmal die Anzahl angeben.\n")
        i = 1
        neueSpieler = []
        while i<=int(anzahl):
            name = input("Wie heißt Spieler " + str(i) + "\n")
            neueSpieler.append(Spieler(name))
            print("Spieler " + str(i) + " heißt nun " + neueSpieler[i-1].name)
            i += 1
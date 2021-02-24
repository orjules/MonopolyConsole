from .Ereigniskarte import Ereigniskarte

class AufFeldGehen(Ereigniskarte):
    zuFeld = None
    darfAufLos = None
    mussDoppeltZahlen = None
    mussInsGefaengnis = None

    def __init__(self, beschreibung, zuFeld, darfAufLos, mussDoppeltZahlen, mussInsGefaengnis):
        self.beschreibung = beschreibung
        self.zuFeld = zuFeld
        self.checkObAufLos = darfAufLos
        self.mussDoppeltZahlen = mussDoppeltZahlen
        self.mussInsGefaengnis = mussInsGefaengnis

    def aktionMachen(self, geradeDran):
        print("Hier wird dann gelaufen")
        # TODO Logik für Aktion erstellen

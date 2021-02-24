from .Ereigniskarte import Ereigniskarte

class GeldZahlen(Ereigniskarte):
    betrag = None

    def __init__(self, beschreibung, betrag):
        self.beschreibung = beschreibung
        self.betrag = betrag

    def aktionMachen(self, geradeDran):
        print("Hier wird dann gezahlt")
        # TODO Logik für Aktion erstellen
from .Grundstueck import Grundstueck

class Bahnhof(Grundstueck):

    def __init__(self, name, feld):
        self.name = name
        self.feld = feld
        self.grundstueckWert = 200
        self.hypothekWert = 100

    def mieteBerechnen(self, anzahlBahnhofe):
        if anzahlBahnhofe == 1:
            return 25
        elif anzahlBahnhofe == 2:
            return 50
        elif anzahlBahnhofe == 3:
            return 100
        elif anzahlBahnhofe == 4:
            return 200
        else:
            return 0
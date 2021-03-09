from .GeldTauschen import GeldTauschen

class GeldOderKarte(GeldTauschen):
    def __init__(self, beschreibung, betrag):
        self.beschreibung = beschreibung
        self.betrag = betrag
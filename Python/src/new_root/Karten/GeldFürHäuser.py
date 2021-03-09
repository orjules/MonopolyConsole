from .GeldTauschen import GeldTauschen

class GeldFürHäuser(GeldTauschen):
    def __init__(self, beschreibung, betrag):
        self.beschreibung = beschreibung
        self.betrag = betrag
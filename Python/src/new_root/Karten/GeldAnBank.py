﻿from .GeldTauschen import GeldTauschen


class GeldAnBank(GeldTauschen):
    def __init__(self, beschreibung, betrag):
        self.beschreibung = beschreibung
        self.betrag = betrag

    def aktionMachen(self, geradeDran):
        geradeDran.kapital -= self.betrag

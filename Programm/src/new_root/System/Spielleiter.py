#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Darsteller import startSequenz

from .Spieler import Spieler
from .Felder import Felder


class Spielleiter:
    spieler = []
    geradeDran = None

    def __init__(self):
        # spieler = self.darsteller.startSequenz()
        self.spieler = [Spieler("Spieler 1", '#'), Spieler("Spieler 2", '!'), Spieler("Spieler 3", '?')]
        self.geradeDran = self.spieler[0]

    def spielerBewegen(self, zusammen):
        neuePos = self.geradeDran.aktuellePosition.value + zusammen
        if neuePos > len(Felder):
            neuePos -= len(Felder)
        self.geradeDran.aktuellePosition = Felder(neuePos)


    def setPosition(self, neuePos):
        self.geradeDran.aktuellePosition = neuePos
        self.darsteller.karteZeichnen(self.spieler)

    def weiter(self):
        neuerIndex = self.spieler.index(self.geradeDran) + 1
        if neuerIndex >= len(self.spieler):
            neuerIndex -= len(self.spieler)
        self.geradeDran = self.spieler[neuerIndex]
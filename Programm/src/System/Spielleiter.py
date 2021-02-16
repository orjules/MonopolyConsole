#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Darsteller import Darsteller
from .Spieler import Spieler
from .Wuerfel import wuerfeln
from .Felder import Felder


class Spielleiter:
    darsteller = Darsteller()
    spieler = []
    geradeDran = None

    def __init__(self):
        # spieler = self.darsteller.startSequenz()
        self.spieler = [Spieler("Spieler 1", '#'), Spieler("Spieler 2", '!'), Spieler("Spieler 3", '?')]
        self.geradeDran = self.spieler[0]
        self.darsteller.karteZeichnen(self.spieler, None, self.geradeDran)
        self.gameLoop()

    def gameLoop(self):
        while(True):
            self.inputVerarbeitung()
            neuerIndex = self.spieler.index(self.geradeDran) + 1
            if neuerIndex >= len(self.spieler):
                neuerIndex -= len(self.spieler)
            self.geradeDran = self.spieler[neuerIndex]


    def spielerBewegen(self):
        # Würfeln
        ergebnis = wuerfeln()
        zusammen = ergebnis[0] + ergebnis[1]
        # Spieler Bewegen
        neuePos = self.geradeDran.aktuellePosition.value + zusammen
        if neuePos > len(Felder):
            neuePos -= len(Felder)
        self.geradeDran.aktuellePosition = Felder(neuePos)
        # Neue Karte und Würfelergebnis darstellen
        self.darsteller.karteZeichnen(self.spieler, ergebnis, self.geradeDran)

    def inputVerarbeitung(self):
        eingabe = input()
        if eingabe == 'w':
            self.spielerBewegen()


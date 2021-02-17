#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Darsteller import Darsteller
from .Spieler import Spieler
from .Wuerfel import wuerfeln
from .Felder import Felder
from ..Grundstuecke.Grundbuch import feldTypGeben


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
            eingabe = self.darsteller.eingabeAbfragen("Was möchtest du tun?\n""'w' für würfeln\n'ü' für die Übersicht deines Kapitals"
                                                      "\n'z' um deinen Zug zu beenden.", {'w', 'ü', 'z'})
            if eingabe == 'w':
                self.spielerBewegen()
                self.aktionenAufFeld()
            elif eingabe == 'ü':
                self.darsteller.assetsAnzeigen(self.geradeDran)
            elif eingabe == 'z':
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
        self.darsteller.spielerHatGewürfelt(ergebnis, self.geradeDran)
        self.darsteller.karteZeichnen(self.spieler)

    def aktionenAufFeld(self):
        feldTyp = feldTypGeben(self.geradeDran.aktuellePosition)
        if feldTyp is not None:
            print("Willst du " + feldTyp.name + " kaufen?")
        # je nach situation andere Ausgabe
        # self.darsteller.eingabeAbfragen("Du bist auf dem Feld " + feld.name + " gelandet. Was möchtest du tun?\n", {})

    # def kartenAKtionMachen(self):


    def setPosition(self, neuePos):
        self.geradeDran.aktuellePosition = neuePos
        self.darsteller.karteZeichnen(self.spieler)
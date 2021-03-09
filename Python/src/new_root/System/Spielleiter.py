#!/usr/bin/env python
# -*- coding: utf 8 -*-


from .Spieler import Spieler
from .Felder import Felder
from ..Karten import RKG

spieler = [Spieler("Spieler 1", '#'), Spieler("Spieler 2", '!'), Spieler("Spieler 3", '?')]
geradeDran = spieler[0]


def spielerBewegen(wuerfelWert):
    global spieler
    global geradeDran
    neuePos = geradeDran.aktuellePosition.value + wuerfelWert
    if neuePos > len(Felder):
        neuePos -= len(Felder)
        # Bedeutet ich bin über Los gegangen
        RKG.spezialFeld(Felder.Los, geradeDran)

    geradeDran.aktuellePosition = Felder(neuePos)


def setPosition(neuePos):
    global geradeDran
    geradeDran.aktuellePosition = neuePos


def weiter():
    global geradeDran
    global spieler
    neuerIndex = spieler.index(geradeDran) + 1
    if neuerIndex >= len(spieler):
        neuerIndex -= len(spieler)
    geradeDran = spieler[neuerIndex]


def kapitalAendern(spieler, menge):
    spieler.kapital += menge

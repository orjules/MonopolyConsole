#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Spieler import Spieler
from .Wuerfel import wuerfeln
from .Felder import Felder
from prettytable import PrettyTable
from ..Grundstuecke.Grundbuch import alleGrundstueckeVon


def startSequenz():
    # Spieler definieren
    print("Willkommen zu Monopoly im Terminal. \n "
          "Dieses Spiel können 2-4 Spieler mit einer Tastatur spielen. \n")
    anzahl = eingabeAbfragen("Wie viele Spieler werden spielen?", {"2", "3", "4"})
    i = 1
    neueSpieler = {}
    while i <= int(anzahl):
        # Name eingeben
        name = input("Wie heißt Spieler " + str(i) + "\n")

        # Würfeln um später zu sortieren
        wurf = wuerfeln()
        ergebnis = wurf[0] + wurf[1]
        istKeinDuplikat = True
        anzahlGewuerfelt = 1
        while istKeinDuplikat:
            if ergebnis in neueSpieler.values():
                wurf = wuerfeln()
                ergebnis = wurf[0] + wurf[1]
                anzahlGewuerfelt += 1
            else:
                istKeinDuplikat = False

        # Spieler und Wert speichern
        neueSpieler[Spieler(name)] = ergebnis
        print("Spieler " + str(i) + " heißt jetzt " + name + " und hat " + str(anzahlGewuerfelt) +
              " mal gewürfelt und eine " + str(ergebnis) + " für die Reihenfolge bekommen.\n")
        i += 1

    reineSpieler = sorted(neueSpieler, key=neueSpieler.get)
    reineSpieler.reverse()  # Weil der mit dem höchsten Anfangen soll nicht mit dem niedrigsten

    print("Die Spieler sind also: ")
    for spieler in reineSpieler:
        print(spieler.name)

    return reineSpieler


def eingabeAbfragen(text, erwarteteEingabe):
    eingabe = input(text + "\n")
    while True:
        for e in erwarteteEingabe:
            if eingabe == e:
                return eingabe
        eingabe = input("Ungültige Eingabe, bitte noch einmal eingeben.\n")
    return


def spielerHatGewürfelt(wurf, geradeDran):
    if wurf is not None:
        print(
            geradeDran.name + " (" + geradeDran.symbol + ") hat " + str(wurf[0]) + ", " + str(wurf[1]) + " gewürfelt.")


def karteZeichnen(spieler):
    # TODO Console löschen
    t = PrettyTable(["Feld", "Spieler"])
    for feld in Felder:
        spielfiguren = []
        for spielr in spieler:
            if feld.value == spielr.aktuellePosition.value:
                spielfiguren.append(spielr.symbol)
        t.add_row([feld.name, ", ".join(spielfiguren)])
    print(t)


def assetsAnzeigen(geradeDran):
    # TODO Console löschen
    print("Dein Kapital ist: " + str(geradeDran.kapital) + "€.")
    # Grundbuch fragen, was dieser Spieler an Assets hat
    grundstuecke = alleGrundstueckeVon(geradeDran)
    if len(grundstuecke) != 0:
        t = PrettyTable(["Grundstück", "Wert", "Häuseranzahl", "Hat Hotel"])
        for grundstueck in grundstuecke:
            hatHotel = "Nein"
            if grundstueck.hatHotel:
                hatHotel = "Ja"
            t.add_row([grundstueck.name, grundstueck.grundstueckWert, grundstueck.anzahlHaus, hatHotel])
        print(t)
    else:
        print("Du besitzt keine Grundstücke.")

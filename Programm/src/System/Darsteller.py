#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Spieler import Spieler
from .Würfel import würfeln

class Darsteller:

    def startSequenz(self):
        # Spieler definieren
        print("Willkommen zu Monopoly im Terminal. \n "
              "Dieses Spiel können 2-4 Spieler mit einer Tastatur spielen. \n")
        anzahl = self.eingabeAbfragen("Wie viele Spieler werden spielen?", {"2", "3", "4"})
        i = 1
        neueSpieler = {}
        while i <= int(anzahl):
            # Name eingeben
            name = input("Wie heißt Spieler " + str(i) + "\n")

            # Würfeln um später zu sortieren
            wurf = würfeln()
            ergebnis = wurf[0] + wurf[1]
            istKeinDuplikat = True
            anzahlGewürfelt = 1
            while istKeinDuplikat:
                if ergebnis in neueSpieler.values():
                    wurf = würfeln()
                    ergebnis = wurf[0] + wurf[1]
                    anzahlGewürfelt += 1
                else:
                    istKeinDuplikat = False

            # Spieler und Wert speichern
            neueSpieler[Spieler(name)] = ergebnis
            print("Spieler " + str(i) + " heißt jetzt " + name + " und hat " + str(anzahlGewürfelt) +
                  " mal gewürfelt und eine " + str(ergebnis) + " für die Reihenfolge bekommen.\n")
            i += 1


        reineSpieler = sorted(neueSpieler, key=neueSpieler.get)
        reineSpieler.reverse()   # Weil der mit dem höchsten Anfangen soll nicht mit dem niedrigsten

        print("Die Spieler sind also: ")
        for spieler in reineSpieler:
            print(spieler.name)

        return reineSpieler

    def eingabeAbfragen(self, text, erwarteteEingabe):
        eingabe = input(text + "\n")
        while True:
            for e in erwarteteEingabe:
                if eingabe == e:
                    return eingabe
            eingabe = input("Ungültige Eingabe, bitte noch einmal eingeben.\n")
        return
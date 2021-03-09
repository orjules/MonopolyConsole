# RKG = Random Karten Generator
# Externe Imports
from ..System.Felder import Felder
# Karten Imports
from .AufFeldGehen import AufFeldGehen
from .GeldAnBank import GeldAnBank
from .GeldVonBank import GeldVonBank

spezielleKarten = [
    GeldAnBank("Einkommenssteuer. Zahle 200 an die Bank.", 200),
    AufFeldGehen("Gehe direkt in das Gefängnis. Gehe nicht über los. Ziehe nicht 200 ein.",
                 Felder.GefaengnisBzwZuBesuch,
                 False, False, True),
    GeldVonBank("Du bist über Los gegangen und hast 200€ eingezogen.", 200)
]

randomKarten = [
    GeldAnBank("Platzhalter für die random Karten.", 0)
]


def karteZiehen(speziellesFeld):
    if speziellesFeld is Felder.Gemeinschaftsfeld1 or Felder.Ereignisfeld1:  # or muss so weiter geführt werden
        return randomKarten[0]
        # TODO wirklich die Random Karten wählen
    else:
        return spezialFeld(speziellesFeld)


def spezialFeld(feld):
    gewaehlteKarte = None
    if feld is Felder.Los:
        gewaehlteKarte = spezielleKarten[2]
    if feld is Felder.Einkommensteuer:
        gewaehlteKarte = spezielleKarten[0]
    return gewaehlteKarte

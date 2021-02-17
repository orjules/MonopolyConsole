# RKG = Random Karten Generator
from .AufFeldGehen import AufFeldGehen
from .GeldZahlen import GeldZahlen
from ..System.Felder import Felder

spezielleKarten = [
    GeldZahlen("Einkommenssteuer. Zahle 200 an die Bank.", 200),
    AufFeldGehen("Gehe direkt in das Gefängnis. Gehe nicht über los. Ziehe nicht 200 ein.", Felder.GefaengnisBzwZuBesuch,
                 False, False, True)
]

randomKarten = [
    GeldZahlen("Platzhalter für die random Karten.", 0)
]



def karteZiehen(speziellesFeld):
    if speziellesFeld is Felder.Gemeinschaftsfeld1 or Felder.Ereignisfeld1: # or muss so weiter geführt werden
        return randomKarten[0]
        # TODO wirklich die Random Karten wählen
    else:
        return spezialFeld(speziellesFeld)


def spezialFeld(feld):
    # TODO 'Los' gesondert implementieren
    if feld is Felder.Einkommensteuer:
        return spezielleKarten[0]
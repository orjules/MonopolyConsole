from .Straße import Strasse
from ..System.Felder import Felder
from .Farbe import Farben
from .Farbgruppe import Farbgruppe

# Liste aller Grundstücke
alleGrundstuecke = [
    Strasse(Felder.Badstrasse.name, Felder.Badstrasse, 60, 30, Farben.Braun, 2, 10, 30, 90, 160, 250, 50),
    Strasse(Felder.Turmstrasse.name, Felder.Turmstrasse, 60, 30, Farben.Braun, 4, 20, 60, 180, 320, 450, 50)

]

alleFarbgruppen = {
    Farbgruppe(Farben.Braun, [alleGrundstuecke[0], alleGrundstuecke[1]])
}


def feldTypGeben(feld):
    # Nimmt Feld und gibt Grundstück oder Aktionsfeld zurück
    for grundstueck in alleGrundstuecke:
        if feld is grundstueck.feld:
            return grundstueck
    # hier können nur Straßen, Werke und Bahnhöfe zurückgegeben werden. Alles andere bringt None




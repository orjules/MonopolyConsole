from .Straße import Strasse
from .Bahnhof import Bahnhof
from ..System.Felder import Felder
from .Farbe import Farben
from .Farbgruppe import Farbgruppe

# Liste aller Grundstücke
alleGrundstuecke = [
    Strasse(Felder.Badstrasse.name, Felder.Badstrasse, 60, 30, Farben.Braun, 2, 10, 30, 90, 160, 250, 50),
    Strasse(Felder.Turmstrasse.name, Felder.Turmstrasse, 60, 30, Farben.Braun, 4, 20, 60, 180, 320, 450, 50),
    Bahnhof(Felder.Suedbahnhof.name, Felder.Suedbahnhof),
    Strasse(Felder.Chaussestrasse.name, Felder.Chaussestrasse, 100, 50, Farben.Blau, 6, 30, 90, 270, 400, 550, 50),
    Strasse(Felder.Elisenstrasse.name, Felder.Elisenstrasse, 100, 50, Farben.Blau, 6, 30, 90, 270, 400, 550, 50),
    Strasse(Felder.Poststrasse.name, Felder.Poststrasse, 120, 60, Farben.Blau, 8, 40, 100, 300, 450, 600, 50)
]

alleFarbgruppen = {
    Farbgruppe(Farben.Braun, [alleGrundstuecke[0], alleGrundstuecke[1]]),
    Farbgruppe(Farben.Blau, [alleGrundstuecke[3], alleGrundstuecke[4], alleGrundstuecke[5]])
}

grundbuch = {
    alleGrundstuecke[0] : None,
    alleGrundstuecke[1] : None,
    alleGrundstuecke[2] : None,
    alleGrundstuecke[3] : None,
    alleGrundstuecke[4] : None,
    alleGrundstuecke[5] : None,
}


def checkObGrundstueck(feld):
    # Nimmt Feld und gibt Grundstück oder Aktionsfeld zurück
    for grundstueck in alleGrundstuecke:
        if feld is grundstueck.feld:
            return grundstueck
    # hier können nur Straßen, Werke und Bahnhöfe zurückgegeben werden. Alles andere bringt None

def checkBesitzer(grundstueck):
    return grundbuch.get(grundstueck)



from .AufFeldGehen import AufFeldGehen
from ..System.Felder import Felder

class GeheInsGefaengnis(AufFeldGehen):
    beschreibung = "Gehe direkt in das Gefängnis. Gehe nicht über los. Ziehen nicht 200€ ein."
    zuFeld = Felder.GefaengnisBzwZuBesuch
    checkObAufLos = False

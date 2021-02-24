# Der eine Spielleiter
from MonopolyConsole.Programm.src.new_root.System.Spielleiter import Spielleiter

# Funktionen vom Darsteller
from .System.Darsteller import eingabeAbfragen as Darsteller_EingabeFragen
from .System.Darsteller import spielerHatGewürfelt as Darsteller_geworfen
from .System.Darsteller import karteZeichnen as Darsteller_KarteZeichnen
from .System.Darsteller import assetsAnzeigen as Darsteller_Assets

# Funktion vom Würfel
from .System.Wuerfel import wuerfeln

# Funktion vom Grundbuch bzw Grundstück
from .Grundstuecke.Grundbuch import checkObGrundstueck as Grundbuch_CheckObGrundstueck
from .Grundstuecke.Grundbuch import checkBesitzer as Grundbuch_CheckBesitzer
from .Grundstuecke.Grundbuch import uebertragen as Grundbuch_Uebertragen
from .Grundstuecke.Grundstueck import Grundstueck
from .Grundstuecke.Straße import Strasse

# Funktion vom Random Karten Generator bzw Karten
from .Karten.RKG import karteZiehen as RKG_KarteZiehen
from .Karten.Ereigniskarte import Ereigniskarte

spielleiter = Spielleiter()

def gameLoop():
    while (True):
        fertig = False
        beendet = False
        pasch = False
        anzahlPasche = 0

        # Als erstes wird die Karte gezeichnet
        Darsteller_KarteZeichnen(spielleiter.spieler)

        # Es wird so lange nach einer Eingabe verlangt, bis gewürfelt wird
        if spielleiter.geradeDran.istImGefaengnis:
            pass
            # hier soll stehen "Bezahlen oder würfeln"
        eingabe = Darsteller_EingabeFragen(spielleiter.geradeDran.name + " (" + spielleiter.geradeDran.symbol
                                           + ") ist dran. Als erstes musst du würfeln.\nDrücke 'w'", {'w'})
        pasch = laufen()

        # Falls man auf eine Karte mit einer Aktion gekommen ist muss die erst ausgeführt werden
        aktionsFeld = aktionFeststellen()

        # Nach dem Würfeln kann man so lange man will Dinge tun, kann aber erst den Zug beenden, wenn das erzwungene getan ist
        while not (beendet):
            frage = ""
            erlaubteEingabe = []

            # Aktionsfeld
            frage = aktionAufforderung(aktionsFeld)
            erlaubteEingabe.append('a')

            # evtl pash geworfen
            if pasch:
                frage = frage + "\n'w' um noch einmal zu würfeln"
                erlaubteEingabe.append('w')

            # Standart Aktionen, also übersicht und Tausch
            frage = frage + "\n'ü' für die Übersicht deines Kapitals"
            erlaubteEingabe.append('ü')
            # TODO Tausch implementieren

            # evtl zug beenden möglich
            if fertig:
                frage = frage + "\n'z' um den Zug zu beenden"
                erlaubteEingabe.append('z')

            # Eingabe fordern
            eingabe = Darsteller_EingabeFragen(frage, erlaubteEingabe)

            # Eingabe verarbeiten
            if eingabe == 'z':
                beendet = True
            elif eingabe == 'ü':
                Darsteller_Assets(spielleiter.geradeDran)
            elif eingabe == 'w':
                anzahlPasche += 1
                if anzahlPasche == 3:
                    pass
                    # gehe ins Gefängnis
            elif eingabe == 'a':
                aktionenAufFeld(aktionsFeld)

def laufen():
    wurf = wuerfeln()
    spielleiter.spielerBewegen(wurf[0] + wurf[1])
    Darsteller_geworfen(wurf, spielleiter.geradeDran)
    Darsteller_KarteZeichnen(spielleiter.spieler)
    if wurf[0] == wurf[1]:
        return True
    else:
        return False

def aktionFeststellen():
    # ist es ein Grundstück?
    grundstueck = Grundbuch_CheckObGrundstueck(spielleiter.geradeDran.aktuellePosition)
    if grundstueck is not None:
        return grundstueck
    # ist eine Ereignisfeld oder ein spezielles Feld?
    feld = RKG_KarteZiehen(spielleiter.geradeDran.aktuellePosition)
    if feld is not None:
        return feld
    # hier wäre etwas falsch gelaufen
    if feld is None and grundstueck is None:
        print("Undefiniertes Feld!!!")

def aktionAufforderung(aktionsfeld):
    # Hier soll festgestellt werden auf welchem Feld man sich befindet und was man da tun kann
    ausgabe = ""
    if isinstance(aktionsfeld, (Grundstueck, Strasse)):
        ausgabe = ausgabe + "Du bist auf " + aktionsfeld.name + " gelandet. "
        if Grundbuch_CheckBesitzer(aktionsfeld) is None:
            ausgabe = ausgabe + "Möchstest du es für " + str(aktionsfeld.grundstueckWert) + "€ kaufen?"
            ausgabe = ausgabe + "\nDein momentaner Kontostand ist " + str(spielleiter.geradeDran.kapital) + "€."
            if spielleiter.geradeDran.kapital >= aktionsfeld.grundstueckWert:
                ausgabe = ausgabe +"\n'a' um das Grundstück zu kaufen."
            else:
                ausgabe = ausgabe + "\nDu hast nicht genug Geld um das Grundstück zu kaufen."
        else:
            pass
            # TODO Miete zahlen implementieren
    elif isinstance(aktionsfeld, Ereigniskarte):
        ausgabe = ausgabe + aktionsfeld.beschreibung
    return ausgabe

def aktionenAufFeld(aktionsfeld):
    if isinstance(aktionsfeld, (Grundstueck, Strasse)):
        if Grundbuch_CheckBesitzer(aktionsfeld) is None:
            if spielleiter.geradeDran.kapital >= aktionsfeld.grundstueckWert:
                Grundbuch_Uebertragen(aktionsfeld, None, spielleiter.geradeDran)
        else:
            pass
    # aktionsfeld.aktionMachen(spielleiter.geradeDran)
    # Je nach Feld eine andere Aktion ausführen

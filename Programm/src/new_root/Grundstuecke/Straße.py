from MonopolyConsole.Programm.src.new_root.Grundstuecke.Grundstueck import Grundstueck


class Strasse(Grundstueck) :
    farbe = None
    mieteAllein = None
    mieteEinHaus = None
    mieteZweiHaus = None
    mieteDreiHaus = None
    mieteVierHaus = None
    mieteHotel = None
    baukostenHaus = None

    anzahlHaus = 0
    hatHotel = False

    def __init__(self, name, feld, grundstueckWert, hypothekWert, farbe, mieteAllein, mieteEinHaus,
                 mieteZweiHaus, mieteDreiHaus, mieteVierHaus, mieteHotel, baukostenHaus):
        self.name = name
        self.feld = feld
        self.grundstueckWert = grundstueckWert
        self.hypothekWert = hypothekWert
        self.farbe = farbe
        self.mieteAllein = mieteAllein
        self.mieteEinHaus = mieteEinHaus
        self.mieteZweiHaus = mieteZweiHaus
        self.mieteDreiHaus = mieteDreiHaus
        self.mieteVierHaus = mieteVierHaus
        self.mieteHotel = mieteHotel
        self.baukostenHaus = baukostenHaus

class Farbgruppe:
    farbe = None
    strassen = None
    istKomplett = False

    def __init__(self, farbe, strassen):
        self.farbe = farbe
        self.strassen = strassen

    # Funktion definieren, die überprüft ob alle Straßen einer Person gehören

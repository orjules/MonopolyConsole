#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Darsteller import Darsteller
from .Spieler import Spieler


class Spielleiter:
    darsteller = Darsteller()
    spieler = []

    def __init__(self):
        # spieler = self.darsteller.startSequenz()
        spieler = [Spieler("Spieler 1", '#'), Spieler("Spieler 2", '!')]
        self.darsteller.karteZeichnen(spieler);



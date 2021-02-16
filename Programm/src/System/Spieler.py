#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Felder import Felder


class Spieler:
    name = None
    aktuellePosition = Felder.Los
    istImGefängnis = False
    kapital = 1500
    grundStücke = None

    def __init__(self, name):
        self.name = name

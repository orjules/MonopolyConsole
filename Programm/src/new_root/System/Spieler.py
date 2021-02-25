#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Felder import Felder


class Spieler:
    name = None
    symbol = None
    aktuellePosition = Felder.Los
    istImGefaengnis = False
    kapital = 1500

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

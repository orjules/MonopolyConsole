#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Felder import Felder


class Spieler:
    name = None
    aktuellePosition = Felder.Los
    istImGefaengnis = False
    kapital = 1500
    grundStuecke = None

    def __init__(self, name):
        self.name = name

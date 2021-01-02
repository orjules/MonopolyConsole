#!/usr/bin/env python
# -*- coding: utf 8 -*-

from .Darsteller import Darsteller


class Spielleiter:
    darsteller = Darsteller()
    spieler = []

    def __init__(self):
        spieler = self.darsteller.startSequenz()



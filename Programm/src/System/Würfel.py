#!/usr/bin/env python
# -*- coding: utf 8 -*-

from random import randint

def würfeln():
    würfelEins = randint(1, 6)
    würfelZwei = randint(1, 6)
    return (würfelEins, würfelZwei)

'''
class Würfel:
    def würfeln(self):
        würfelEins = randint(1, 6)
        würfelZwei = randint(1, 6)
        return (würfelEins, würfelZwei)
'''
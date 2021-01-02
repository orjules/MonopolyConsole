import unittest
from ...src.System.Darsteller import Darsteller

class DarstellerTest(unittest.TestCase):

    darsteller = Darsteller()

    #def test_eingabeAbfragen(self):
     #   self.assertEqual(self.darsteller.eingabeAbfragen("TestEingabe, Erwartet wird: a", {"a", "b", "c"}),
      #                   "a", "Eingabe muss 'a' sein.")
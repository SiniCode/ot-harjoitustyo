import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_konstruktori_asettaa_saldon_oikein(self):
        kortti = Maksukortti(10)
        self.assertEqual(str(kortti), "Kortilla on rahaa 9 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti = Maksukortti(10)

        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 7.5 euroa")

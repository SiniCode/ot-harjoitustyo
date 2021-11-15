import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(kortti), "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        kortti.syo_maukkaasti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti.syo_maukkaasti()
        kortti.syo_maukkaasti()
        # nyt kortin saldo on 2
        kortti.syo_edullisesti()
        self.assertEqual(str(kortti), "Kortilla on rahaa 2 euroa")

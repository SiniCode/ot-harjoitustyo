import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 14.0")

    def test_maksu_onnistuu_jos_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_ota_rahaa_palauttaa_True_jos_onnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(400), True)

    def test_ota_rahaa_palauttaa_False_jos_rahat_eivat_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)

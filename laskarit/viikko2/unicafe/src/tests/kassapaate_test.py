import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti1 = Maksukortti(400)
        self.kortti2 = Maksukortti(200)

    def test_luodussa_kassassa_tuhat_euroa(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_luodussa_kassassa_nolla_edullista_lounasta(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_luodussa_kassassa_nolla_maukasta_lounasta(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kateisosto_kasvattaa_kassan_rahamaaraa_oikein(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_edullisesta_kateisostoksesta_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)

    def test_edullinen_kateisosto_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_kateisosto_kasvattaa_kassan_rahamaaraa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_maukkaasta_kateisostoksesta_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_maukas_kateisosto_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kassan_rahamaara_ei_muutu_jos_kateinen_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kaikki_rahat_palautetaan_jos_kateinen_ei_riita_edulliseen(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

    def test_myytyjen_lounaiden_maara_ei_muutu_jos_kateinen_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kassan_rahamaara_ei_muutu_jos_kateinen_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kaikki_rahat_palautetaan_jos_kateinen_ei_riita_maukkaaseen(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(350), 350)

    def test_myytyjen_lounaiden_maara_ei_muutu_jos_kateinen_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_korttiosto_palauttaa_True(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti1), True)

    def test_edullinen_korttiosto_ei_kasvata_kassan_rahamaaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullinen_korttiostos_laskee_kortin_saldoa_oikein(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), "saldo: 1.6")

    def test_edullinen_korttiosto_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti1)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_maukas_korttiosto_palauttaa_True(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti1), True)

    def test_maukas_korttisosto_ei_kasvata_kassan_rahamaaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukas_korttiostos_laskee_kortin_saldoa_oikein(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(str(self.kortti1), "saldo: 0.0")

    def test_maukas_korttisosto_kasvattaa_myytyjen_lounaiden_maaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti1)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_edullinen_korttiosto_palauttaa_False_jos_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti2), False)

    def test_kassan_rahamaara_ei_muutu_jos_saldo_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortin_saldo_ei_muutu_jos_saldo_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(str(self.kortti2), "saldo: 2.0")

    def test_myytyjen_lounaiden_maara_ei_muutu_jos_saldo_ei_riita_edulliseen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti2)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_korttiosto_palauttaa_False_jos_saldo_ei_riita(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti2), False)

    def test_kassan_rahamaara_ei_muutu_jos_saldo_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortin_saldo_ei_muutu_jos_saldo_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(str(self.kortti2), "saldo: 2.0")

    def test_myytyjen_lounaiden_maara_ei_muutu_jos_saldo_ei_riita_maukkaaseen(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti2)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_rahan_lataaminen_kortille_kasvattaa_saldoa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti1, 600)
        self.assertEqual(str(self.kortti1), "saldo: 10.0")

    def test_rahan_lataaminen_kortille_kasvattaa_kassaa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti1, 600)
        self.assertEqual(self.kassa.kassassa_rahaa, 100600)

    def test_negatiivisen_summan_lataaminen_kortille_ei_muuta_saldoa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti1, -200)
        self.assertEqual(str(self.kortti1), "saldo: 4.0")

    def test_negatiivisen_summan_lataaminen_kortille_ei_muuta_kassan_rahamaaraa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti1, -200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

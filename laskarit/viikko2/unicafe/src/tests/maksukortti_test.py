import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_kortin_lataaminen_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_rahan_ottaminen_onnistuu_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_rahan_ottaminen_ei_onnistu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_rahan_ottaminen_palauttaa_true_jos_rahaa_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(8), True)

    def test_rahan_ottaminen_palauttaa_false_jos_rahaa_ei_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)

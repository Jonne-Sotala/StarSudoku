import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassan_rahan_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_luodun_kassan_edullisten_myynti_on_nolla(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_luodun_kassan_maukkaiden_myynti_on_nolla(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_rahamaara_on_oikea_edullisen_oston_jalkeen_kun_maksu_riitti(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_vaihtoraha_on_oikea_edullisen_oston_jalkeen_kun_maksu_riitti(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)

    def test_lounaiden_maara_on_oikea_edullisen_oston_jalkeen_kun_maksu_riitti(self):
        self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_rahamaara_on_oikea_edullisen_oston_jalkeen_kun_maksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_vaihtoraha_on_oikea_edullisen_oston_jalkeen_kun_maksu_ei_riita(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_lounaiden_maara_on_oikea_edullisen_oston_jalkeen_kun_maksu_ei_riita(self):
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_rahamaara_on_oikea_maukkaan_oston_jalkeen_kun_maksu_riitti(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_vaihtoraha_on_oikea_maukkaan_oston_jalkeen_kun_maksu_riitti(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)

    def test_lounaiden_maara_on_oikea_maukkaan_oston_jalkeen_kun_maksu_riitti(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_rahamaara_on_oikea_maukkaan_oston_jalkeen_kun_maksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_vaihtoraha_on_oikea_maukkaan_oston_jalkeen_kun_maksu_ei_riita(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(390)
        self.assertEqual(vaihtoraha, 390)

    def test_lounaiden_maara_on_oikea_maukkaan_oston_jalkeen_kun_maksu_ei_riita(self):
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_veloitus_toimii_edullisessa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_palautetaan_true_edullisessa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))

    def test_edullisten_myynti_kasvaa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_ei_veloiteta_edullisessa_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 200)

    def test_palautetaan_false_edullisessa_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(self.kortti))

    def test_edullisten_myynti_ei_kasva_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_veloitus_toimii_maukkaassa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_palautetaan_true_maukkaassa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))

    def test_maukkaiden_myynti_kasvaa_korttiostossa_kun_tarpeeksi_rahaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_ei_veloiteta_maukkaassa_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 200)

    def test_palautetaan_false_maukkaassa_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(self.kortti))

    def test_maukkaiden_myynti_ei_kasva_korttiostossa_kun_raha_ei_riita(self):
        self.kortti.saldo = 200
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttia_ladattaessa_kassan_rahat_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 2000)
        self.assertEqual(self.kassa.kassassa_rahaa, 102000)

    def test_kortti_ladattaessa_kortin_saldo_kasvaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 2000)
        self.assertEqual(self.kortti.saldo, 3000)

    def test_kortti_ei_lataudu_negatiivisella_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kortti.saldo, 1000)

    def test_kassan_rahat_eivat_muutu_negatiivisella_kortin_latauksella(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luotu_kassapaate_oikeat_arvot(self):
        # [raha, edulliset, maukkaat]
        testi = [self.kassapaate.kassassa_rahaa,self.kassapaate.edulliset,self.kassapaate.maukkaat]
        self.assertEqual(testi, [100000,0,0])
    
    def test_maukas_vaihtoraha(self):
        self.assertEqual(100, self.kassapaate.syo_maukkaasti_kateisella(500))

    def test_edullisesti_vaihtoraha(self):
        self.assertEqual(260, self.kassapaate.syo_edullisesti_kateisella(500))

    def test_kassan_raha_kasvaa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(100640, self.kassapaate.kassassa_rahaa)

    def test_maksu_riittava_kateisella(self):
        # vaihtoraha, vaihtoraha, edulliset+maukkaat
        testi =[]
        testi.append(self.kassapaate.syo_maukkaasti_kateisella(100))
        testi.append(self.kassapaate.syo_edullisesti_kateisella(100))
        testi.append(self.kassapaate.edulliset + self.kassapaate.maukkaat)
        self.assertEqual([100,100,0], testi)

    def test_lounaat_kasvaa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 2)
    
    def test_lounaat_kasvaa_kortilla(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual( self.kassapaate.edulliset+self.kassapaate.maukkaat , 2)

    def test_veloitetaan_raha_kortilta(self):
        maksukortti = Maksukortti(1000)
        palautus_toimii = self.kassapaate.syo_edullisesti_kortilla(maksukortti) and self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        maksukortti.saldo
        self.assertEqual((True, 360),(palautus_toimii,maksukortti.saldo))

    def test_kortilla_ei_tarpeeksi_rahaa(self):
        maksukortti = Maksukortti(100)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti) or self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual((100, False, 0), (maksukortti.saldo, palautus, self.kassapaate.edulliset + self.kassapaate.maukkaat))
    
    def test_saldo_lataus(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual([100100,100],[self.kassapaate.kassassa_rahaa,maksukortti.saldo])
    
    def test_saldo_lataus_neg_arvolla(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual([100000, 0],[self.kassapaate.kassassa_rahaa,maksukortti.saldo])
        
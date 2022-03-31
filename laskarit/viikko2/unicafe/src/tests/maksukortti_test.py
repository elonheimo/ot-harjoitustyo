import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_lataa_rahaa_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_ota_rahaa_vahentaa_saldoa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_ota_rahaa_ei_vahenna_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")


#    def test_ota_rahaa_ei_toimi_neg_arvolla(self):
#        self.maksukortti.ota_rahaa(-500)
#        self.assertEqual(str(self.maksukortti), "saldo: 10.0")



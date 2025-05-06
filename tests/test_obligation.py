import unittest
from src.instruments.obligation import Obligation

class TestObligation(unittest.TestCase):

    def test_calcul_prix(self):
        oblig = Obligation("Test", 5, 5.0, 1, 100)
        prix = oblig.calculer_prix(0.04)
        self.assertAlmostEqual(prix, 1045.95, delta=2.0)

    def test_obtenir_flux(self):
        oblig = Obligation("Test", 5, 5.0, 1, 100)
        flux = oblig.obtenir_flux()
        self.assertEqual(len(flux), 5)
        self.assertAlmostEqual(flux[-1], 1050.0, delta=0.01)

    def test_calcul_ytm(self):
        oblig = Obligation("Test", 5, 5.0, 1, 1045.95)
        ytm = oblig.calculer_ytm()
        self.assertAlmostEqual(ytm, 0.04, delta=0.001)

if __name__ == '__main__':
    unittest.main()

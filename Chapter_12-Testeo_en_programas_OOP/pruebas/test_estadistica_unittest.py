from lista_estadistica import ListaEstadistica
import unittest

class ComprobarInputsValidos(unittest.TestCase):
    def setUp(self):
        self.estadistica = ListaEstadistica([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.estadistica.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.estadistica.median(), 3)
        self.estadistica.append(4)
        self.assertEqual(self.estadistica.median(), 3)

    def test_modes(self):
        self.assertEqual(self.estadistica.mode(), [2,3])
        self.estadistica.remove(2)
        self.assertEqual(self.estadistica.mode(), [3])

if __name__ == "__main__":
    unittest.main()
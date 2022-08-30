import unittest
import sys

class SaltarTest(unittest.TestCase):
    @unittest.expectedFailure
    def test_falla(self):
        self.assertEqual(False, True)

    @unittest.skip("Este test es inutil")
    def test_saltar(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 4, "roto en 3.4")
    def test_saltarSi(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith("linux"), "roto fuera de linux")
    def test_saltarANoSer(self):
        self.assertEqual(False, True)

if __name__ == "__main__":
    unittest.main()
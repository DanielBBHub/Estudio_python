import unittest

def media(secu):
    return sum(secu) / len(secu)


class TestMedia(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, media, [])
    
    def test_con_zero(self):
        with self.assertRaises(ZeroDivisionError):
            media([])


if __name__ == "__main__":
    unittest.main()
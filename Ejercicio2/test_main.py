import unittest

from main import NumeroEntero


class Test(unittest.TestCase):
    def test_numero_entero(self):
        self.assertEqual(True, NumeroEntero(1998))

if __name__ == '__main__':
    unittest.main()
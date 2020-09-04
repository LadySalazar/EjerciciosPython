import unittest

from Ejercicio import saberEdad

class Test(unittest.TestCase):
    def test_saber_edad(self):
        self.assertEqual(72, saberEdad(0, 1998))


if __name__ == '__main__':
    unittest.main()

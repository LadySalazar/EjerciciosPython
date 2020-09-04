import unittest

from main import ImprimirCaracter


class Test(unittest.TestCase):
    def test_imprimir_caracter(self):
        self.assertEqual("Primera letra s y l letra",ImprimirCaracter("sol"))
if __name__ == '__main__':
    unittest.main()
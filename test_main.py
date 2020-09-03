from unittest import TestCase

from main import saberEdad


class Test(TestCase):
    def test_saber_edad(self):
        self.assertEqual(72,saberEdad(0,1998))

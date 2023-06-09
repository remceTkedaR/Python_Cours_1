# program testujący  właściwy plik aplikacji base_1.py
# Opis edycji pliku testowego i jego wstępna inicjalizacja tu:
# https://www.jetbrains.com/help/pycharm/2020.1/test-driven-development-with-twisted.html?utm_campaign=PC&utm_content=2020.1&utm_medium=link&utm_source=product#test
#

from calculus.base_1 import Calculation
from twisted.trial import unittest


class TestCalculation(unittest.TestCase):
    def test_add(self):
        calc = Calculation()
        result = calc.add(3, 8)
        self.assertEqual(result, 11)

    def test_subtract(self):
        calc = Calculation()
        result = calc.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiply(self):
        calc = Calculation()
        result = calc.multiply(12, 5)
        self.assertEqual(result, 60)

    def test_divide(self):
        calc = Calculation()
        result = calc.divide(12, 4)
        self.assertEqual(result, 3)

    def test_modulo(self):
        calc = Calculation()
        result = calc.modulo(55, 6)
        self.assertEqual(result, 1)

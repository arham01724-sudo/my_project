import unittest
from calculator import add , subtract , division , multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5,3),8)

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5,3),8)

class TestCalculator(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divison(5,3),8)

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5,3),8)

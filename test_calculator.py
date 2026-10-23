import unittest
from calculator import add , subtract , division , multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,3),13)
    def test_subtract(self):
        self.assertEqual(subtract(10,4),6)
    def test_division_by_0(self):
        with self.assertRaises(ValueError):
            division(10,0)
    def test_multiply(self):
        self.assertEqual(multiply(6,3),18)

if __name__ == "__main__":
    unittest.main()

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(10, 0)  # This should raise an error

if __name__ == "__main__":
    unittest.main()

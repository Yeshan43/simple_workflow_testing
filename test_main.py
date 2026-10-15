
import unittest

from main import add_numbers


class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add_numbers(10, 0), 10)


if __name__ == "__main__":
    unittest.main()

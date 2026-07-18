"""
Юнит-тесты для factorial.py.

Запуск: python -m unittest test_factorial.py
"""

import unittest
from unittest.mock import patch

from factorial import factorial, get_positive_integer


class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_positive_small(self):
        self.assertEqual(factorial(5), 120)

    def test_positive_large(self):
        # Проверяем, что большие числа обрабатываются без ошибок
        result = factorial(1000)
        self.assertEqual(len(str(result)), 2568)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            factorial(-3)


class TestGetPositiveInteger(unittest.TestCase):
    @patch("builtins.input", side_effect=["7"])
    def test_valid_input(self, mock_input):
        self.assertEqual(get_positive_integer(), 7)

    @patch("builtins.input", side_effect=["abc", "5"])
    def test_non_numeric_then_valid(self, mock_input):
        self.assertEqual(get_positive_integer(), 5)

    @patch("builtins.input", side_effect=["-1", "0", "3"])
    def test_negative_and_zero_then_valid(self, mock_input):
        self.assertEqual(get_positive_integer(), 3)

    @patch("builtins.input", side_effect=["3.5", "4"])
    def test_float_string_then_valid(self, mock_input):
        self.assertEqual(get_positive_integer(), 4)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the function max_integer"""

    def test_max_at_end(self):
        """Test quand le max est à la fin de la liste"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test quand le max est au début"""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Test quand le max est au milieu"""
        self.assertEqual(max_integer([1, 99, 3, 4]), 99)

    def test_one_element(self):
        """Test une liste avec un seul élément"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test une liste vide"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test une liste avec seulement des négatifs"""
        self.assertEqual(max_integer([-5, -9, -3, -8]), -3)

    def test_mixed_numbers(self):
        """Test avec nombres positifs et négatifs"""
        self.assertEqual(max_integer([-5, 10, -2, 7]), 10)

    def test_floats(self):
        """Test avec des nombres flottants"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)


if __name__ == '__main__':
    unittest.main()

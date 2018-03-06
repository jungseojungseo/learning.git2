# -*- coding: utf-8 -*-
import unittest
import x_fizzbuzz
import os

class X_fizzbuzzTestCase(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(x_fizzbuzz.fizzbuzz(10), [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz'])
if __name__ == "__main__":
    unittest.main(verbosity=2)

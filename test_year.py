# -*- coding: utf-8 -*-
import unittest
import x_year

class X_YearTestCase(unittest.TestCase):
    def test_year(self):
        self.assertEqual(x_year.year(2300), '평년')
if __name__ == "__main__":
    unittest.main(verbosity=2)

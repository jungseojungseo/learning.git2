# -*- coding: utf-8 -*-
import unittest
import x_tax

class X_TaxTestCase(unittest.TestCase):
    def test_tax(self):
        self.assertEqual(x_tax.tax(20, 50000, 0), 25000)
if __name__ == "__main__":
    unittest.main(verbosity=2)

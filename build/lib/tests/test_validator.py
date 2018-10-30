import unittest
from pycalc import validator


class TestValidator(unittest.TestCase):
    def test_refactor(self):
        valid = "1D2*3Q3*(1+2)"
        refactored = validator.refactor("1 // 2 * 3 == 3(1 + 2)")

        self.assertEqual(valid, refactored)

    def test_combine_operator(self):
        valid = "-1"
        combined = validator.combine_operator_seq("------+-1")

        self.assertEqual(valid, combined)
        
    def test_split(self):
        valid = [2, "+", 2]
        splitted = validator.split_expression("2+2")
        
        self.assertEqual(valid, splitted)
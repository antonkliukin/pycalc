import unittest
from pycalc.operator_parser import *

class TestOperator(unittest.TestCase):
    def test_is_operator(self):
        for operator in PRIORITY_OPERATORS.keys():
            self.assertTrue(is_operator(operator))

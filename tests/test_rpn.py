import unittest
from pycalc import validator, rpn_formatter


class TestRPN(unittest.TestCase):
    def test_rpn(self):
        initial_value = "2+1*10"
        formatted = rpn_formatter.format(validator.split_expression(initial_value))

        valid = [2.0, 1.0, 10.0, '*', '+']


        self.assertEqual(valid, formatted)




import unittest
from pycalc import calculator
from math import *

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calculator.calculate("1+1")
        self.assertEqual(result, 2)

    def test_unary_operators(self):
        self.assertEqual(-13, calculator.calculate("-13"))
        self.assertEqual(19, calculator.calculate("6-(-13)"))
        self.assertEqual(0, calculator.calculate("1---1"))
        self.assertEqual(-1, calculator.calculate("-+---+-1"))

    def test_operation_priority(self):
        self.assertEqual(5, calculator.calculate("1+2*2"))
        self.assertEqual(25, calculator.calculate("1+(2+3*2)*3"))
        self.assertEqual(30, calculator.calculate("10*(2+1)"))
        self.assertEqual(1000, calculator.calculate("10^(2+1)"))
        self.assertEqual(100 / 3 ** 2, calculator.calculate("100/3^2"))
        self.assertEqual(100 / 3 % 2 ** 2, calculator.calculate("100/3%2^2"))

    def test_functions_and_constants(self):
        self.assertEqual(pi + e, calculator.calculate("pi+e"))
        self.assertEqual(1, calculator.calculate("log(e)"))
        self.assertEqual(1, calculator.calculate("sin(pi/2)"))
        self.assertEqual(2, calculator.calculate("log10(100)"))
        self.assertEqual(sin(pi/2), calculator.calculate("sin(pi/2)"))
        self.assertEqual(2, calculator.calculate("2*sin(pi/2)"))

    def test_associative(self):
        self.assertEqual(102 % 12 % 7, calculator.calculate("102%12%7"))
        self.assertEqual(100 / 4 / 3, calculator.calculate("100/4/3"))
        self.assertEqual(2 ** 3 ** 4, calculator.calculate("2^3^4"))

    def test_comparison_operators(self):
        self.assertEqual(1 + 2 * 3 == 1 + 2 * 3, calculator.calculate("1+2*3==1+2*3"))
        self.assertEqual(e ** 5 >= e ** 5 + 1, calculator.calculate("e^5>=e^5+1"))
        self.assertEqual(1 + 2 * 4 // 3 + 1 != 1 + 2 * 4 // 3 + 2, calculator.calculate("1+24/3+1!=1+24/3+2"))

    def test_common_tests(self):
        self.assertEqual(100, calculator.calculate("(100)"))
        self.assertEqual(666, calculator.calculate("666"))
        self.assertEqual(120, calculator.calculate("10(2+1)4"))
        self.assertEqual(-0.1, calculator.calculate("-.1"))
        self.assertEqual(1. / 3, calculator.calculate("1/3"))
        self.assertEqual(1.0 / 3.0, calculator.calculate("1.0/3.0"))
        self.assertEqual(.1 * 2.0 ** 56.0, calculator.calculate(".1 * 2.0^56.0"))
        self.assertEqual(e ** 34, calculator.calculate("e^34"))
        self.assertEqual((2.0**(pi/pi+e/e+2.0**0.0)), calculator.calculate("(2.0^(pi/pi+e/e+2.0^0.0))"))
        self.assertEqual((2.0**(pi/pi+e/e+2.0**0.0)) ** (1.0/3.0),
                         calculator.calculate("(2.0^(pi/pi+e/e+2.0^0.0))^(1.0/3.0)"))
        self.assertEqual(sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0**2.0))))--cos(1.0)--cos(0.0)**3.0),
                         calculator.calculate("sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0^2.0))))--cos(1.0)--cos(0.0)^3.0)"))
        self.assertEqual(2.0 ** (2.0**2.0*2.0**2.0), calculator.calculate("2.0^(2.0^2.0*2.0^2.0)"))

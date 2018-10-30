#!/usr/bin/python
from pycalc import calculator
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Pure-python command-line calculator.")
    parser.add_argument("EXPRESSION", help="expression string to evaluate", type=str)
    parser.add_argument("-m", "--use-modules", metavar="MODULE", nargs="+", help="additional modules to use")
    args = parser.parse_args()
    return args


def solve(expression):
    result = calculator.calculate(expression)
    return result


def main():
    args = parse_args()
    expression = args.EXPRESSION
    result = solve(expression)
    print("{} =".format(expression), result)

if __name__ == "__main__":
    main()

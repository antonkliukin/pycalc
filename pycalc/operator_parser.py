import math


def is_operator(operator):
    """
    Checks if provided string is operator.
    :param operator: String you want to check.
    :return: Bool value.
    """
    return operator in PRIORITY_OPERATORS


OPENED_BRACKET = '('
CLOSED_BRACKET = ')'
EXPONENTIATION = '^'
MULTIPLICATION = '*'
DIVISION = '/'
DDIVISION = 'D'
MDIVISION = '%'
MINUS = '-'
PLUS = '+'

COS = "cos"
MCOS = "-cos"
SIN = "sin"
MSIN = "-sin"
TAN = "tan"
ASIN = "asin"
ACOS = "acos"
ATAN = "atan"
ATAN2 = "atan2"

SQRT = "sqrt"
ABS = "abs"
LOG = "log"
LOG10 = "lgT"

E = "e"
PI = "pi"

LESSOREQUAL = "K"
LESS = "<"
EQUAL = "Q"
NOTEQUAL = "N"
GREATEROREQUAL = "G"
GREATER = ">"


PRIORITY_OPERATORS = {
    OPENED_BRACKET: float("inf"),
    CLOSED_BRACKET: float("inf"),

    E: 4,
    ABS: 4,
    COS: 4,
    MCOS: 4,
    SIN: 4,
    MSIN: 4,
    TAN: 4,
    ASIN: 4,
    ACOS: 4,
    ATAN: 4,
    ATAN2: 4,

    LOG: 3,
    SQRT: 3,
    LOG10: 3,
    EXPONENTIATION: 3,

    DIVISION: 2,
    DDIVISION: 2,
    MDIVISION: 2,
    MULTIPLICATION: 2,

    PLUS: 1,
    MINUS: 1,

    LESS: 0,
    LESSOREQUAL: 0,
    EQUAL: 0,
    NOTEQUAL: 0,
    GREATEROREQUAL: 0,
    GREATER: 0
}

MAP_OPERATORS = {
    EXPONENTIATION: lambda x, y: x ** y,
    MULTIPLICATION: lambda x, y: x * y,
    DDIVISION: lambda x, y: x // y,
    MDIVISION: lambda x, y: x % y,
    MINUS: lambda x, y: x - y,
    PLUS: lambda x, y: x + y,
    DIVISION: lambda x, y: x / y,

    LESS: lambda x, y: x < y,
    LESSOREQUAL: lambda x, y: x <= y,
    EQUAL: lambda x, y: x == y,
    NOTEQUAL: lambda x, y: x != y,
    GREATER: lambda x, y: x > y,
    GREATEROREQUAL: lambda x, y: x >= y
}

MATH_FUNCTIONS = {
    ATAN2: lambda x: math.atan2(x),
    ATAN: lambda x: math.atan(x),
    ACOS: lambda x: math.acos(x),
    ASIN: lambda x: math.asin(x),
    COS: lambda x: math.cos(x),
    MCOS: lambda x: -math.cos(x),
    SIN: lambda x: math.sin(x),
    MSIN: lambda x: -math.sin(x),
    TAN: lambda x: math.tan(x),
    SQRT: lambda x: math.sqrt(x),
    LOG10: lambda x: log10(x),
    LOG: lambda x: math.log(x),
    ABS: lambda x: abs(x)
}

CONSTANTS = {
    E: math.e,
    PI: math.pi
}

def log10(val):
    try:
        return math.log10(val)
    except ValueError:
        print('Value error.')
        return 0

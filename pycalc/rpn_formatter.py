from pycalc.operator_parser import *
from pycalc import calculator


def format(expression):
    """
    Returns expression in rpn format.
    :param expression: Expression in splitted format (ex: ["1", "+", "2"])
    :return:
    """

    stack_operators = []
    stack = []

    for token in expression:
        if type(token) is list:
            func = token[0]
            sub_expression = token[1]
            stack.append(MATH_FUNCTIONS[func](calculator.calculate_rpn_expression(format(sub_expression))))
        elif is_operator(token):
            if CLOSED_BRACKET == token:
                tmp = stack_operators.pop()
                while OPENED_BRACKET != tmp:
                    stack.append(tmp)
                    tmp = stack_operators.pop()
            elif OPENED_BRACKET == token:
                stack_operators.append(token)
            else:
                if len(stack_operators):
                    if PRIORITY_OPERATORS[token] <= PRIORITY_OPERATORS[stack_operators[-1]]:
                        if OPENED_BRACKET != stack_operators[-1]:
                            stack.append(stack_operators.pop())
                stack_operators.append(token)
        else:
            stack.append(token)

    while len(stack_operators) > 0:
        stack.append(stack_operators.pop())

    return stack

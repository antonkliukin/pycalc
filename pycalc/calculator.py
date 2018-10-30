from pycalc.operator_parser import *
from pycalc import validator, rpn_formatter as formatter


def calculate(expression):
    """
    Evaluate expression.
    :param expression:
    :return: Result of expression.
    """
    assert len(expression) > 0, "ERROR: Expression is missing."

    expression = validator.refactor(expression)
    expression = validator.split_expression(expression)

    formatted_expression = formatter.format(expression)


    return calculate_rpn_expression(formatted_expression)


def calculate_rpn_expression(formatted_expression):
    """
    Evaluate expression in rpn format.
    :param expression:
    :return: Result of expression.
    """

    length = len(formatted_expression)
    i = 0

    while i < length:
        token = formatted_expression[i]

        if token in ["<", ">", "K", "G", "Q", "N"] and not i == length - 1:
            formatted_expression.append(formatted_expression[i - 1])
            formatted_expression.append(token)
            formatted_expression = formatted_expression[:i - 1] + formatted_expression[
                                                                  formatted_expression.index(token) + 1:]
            i = i - 1

            continue

        if token in MAP_OPERATORS:
            index_right_operand = i - 2
            index_left_operand = i - 1
            try:
                res = MAP_OPERATORS[token](formatted_expression[index_right_operand],
                                           formatted_expression[index_left_operand])
            except ArithmeticError:
                res = 0
            formatted_expression.insert(i + 1, res)
            formatted_expression = formatted_expression[:index_right_operand] + formatted_expression[i + 1:]
            length = len(formatted_expression)
            j = formatted_expression.index(res)
            i = j + 1

            if j > length:
                break
            continue
        i += 1

    result = formatted_expression[0]

    return result

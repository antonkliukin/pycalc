from pycalc.operator_parser import *


def is_stop_parsing_operand(ch):
    return ch.isspace() or is_operator(ch)


def is_opened_bracket(ch):
    return OPENED_BRACKET == ch


def is_closed_bracket(ch):
    return CLOSED_BRACKET == ch


def refactor(string: str) -> str:
    """
    Removes spaces, format operators (ex.: // -> D), add * between )(
    """

    string = string.replace(" ", "")
    string = combine_operator_seq(string)

    string = string.replace('//', 'D')
    string = string.replace('log10', 'lgT')
    string = string.replace('>=', 'G')
    string = string.replace('<=', 'K')
    string = string.replace('==', 'Q')
    string = string.replace('!=', 'N')

    string = string.replace('e', str(CONSTANTS['e']))
    string = string.replace('pi', str(CONSTANTS['pi']))

    i = 0
    while i < len(string) - 1:
        if (string[i].isnumeric() or string[i] == '.') and string[i + 1] == '(':
            string = string[0:i + 1] + '*' + string[i + 1:]
        elif string[i] == ')' and (string[i + 1].isnumeric() or string[i + 1] == '.'):
            string = string[0:i + 1] + '*' + string[i + 1:]
        elif string[i] == '^':
            expression = ''
            index = i

            while index < len(string) - 1:
                if string[index + 1].isnumeric():
                    expression = expression + string[index + 1]
                elif string[index + 1] == '^':
                    expression = expression + string[index + 1]
                else:
                    break

                index += 1

            if '^' in expression:
                string = string[:i + 1] + '(' + expression + ')' + string[index + 1:]

            "2^3^4"

        i += 1

    # string = add_brackets(string)

    return string


def add_brackets(string: str) -> str:
    start_index = 0
    end_index = 0
    while start_index <= len(string) - 1:
        if string[start_index] in ["-", "+"] and string[start_index + 1].isdigit() and \
                not string[start_index - 1].isdigit() and not string[start_index - 1] == ')':
            number = string[start_index] + string[start_index + 1]
            end_index = start_index + 1

            for index in range(start_index + 2, len(string)):
                try:
                    float(number + string[index])
                except ValueError:
                    break

                number = number + string[index]
                end_index += 1

            string = string[:start_index] + "(" + number + ")" + string[end_index + 1:]

            start_index = end_index
        start_index += 1

    return string


# (10*(e^0)*log10(.4-(5/(-0.1))-10))+abs((-53)/10)-5


def combine_operator_seq(string: str) -> str:
    """
    Combine operators sequence.
    Ex: "---1" -> "-1"
    """
    for i in range(0, len(string) - 1):
        if i >= len(string):
            return string

        if string[i] in ["-", "+"] and string[i + 1] in ["-", "+"]:
            current = string[i]
            if current == "-" and string[i + 1] == "-":
                current = "+"
            elif current == "-" or string[i + 1] == "-":
                current = "-"
            else:
                return string

            string = string[:i] + current + string[i + 2:]
            string = combine_operator_seq(string)

    return string


def split_expression(string):
    """
    Returns slitted expression in format [2, "+", 2]
    """

    def _process_operand(index):
        supposed_operand = string[index]
        index += 1
        while index < length and not is_stop_parsing_operand(string[index]):
            supposed_operand += string[index]
            index += 1
        try:
            if supposed_operand in MATH_FUNCTIONS:
                brackets_counter = 1
                index += 1
                begin = index
                while index < length and brackets_counter != 0:
                    if OPENED_BRACKET == string[index]:
                        brackets_counter += 1
                    elif CLOSED_BRACKET == string[index]:
                        brackets_counter -= 1
                    index += 1
                expression.append([supposed_operand, split_expression(string[begin:index - 1])])
            elif supposed_operand in CONSTANTS:
                expression.append(float(CONSTANTS[supposed_operand]))
            else:
                expression.append(float(supposed_operand))
        except ValueError:
            raise Exception("ERROR: '{}' is not operand".format(supposed_operand))
        return index

    def _process_operator(index):
        supposed_operator = string[index]  # assume that length of operator should be equal to one
        if is_operator(supposed_operator):
            expression.append(supposed_operator)
        else:
            raise Exception("ERROR: '{}' is not operator".format(supposed_operator))
        return index + 1

    def _skip_spaces(index):
        while index < length and string[index].isspace():
            index += 1
        return index

    length = len(string)
    is_operand_flag = True
    expression = []
    i = 0

    while True:
        i = _skip_spaces(i)
        if i >= length:
            break
        if is_opened_bracket(string[i]):
            is_operand_flag = False
        elif is_closed_bracket(string[i]):
            is_operand_flag = False
            i = _process_operator(i)
            continue

        if is_operand_flag:
            i = _process_operand(i)
        else:
            i = _process_operator(i)
        is_operand_flag = not is_operand_flag

    return expression

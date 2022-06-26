import pytest

from rpn.calc import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def verify_answer(expected, answer):
    assert expected == answer


# simple test case for each function
@pytest.mark.functest
def test_add(calculator):
    answer = calculator.calculate_rpn("2 3 +")
    verify_answer(5, answer)


@pytest.mark.functest
def test_subtract(calculator):
    answer = calculator.calculate_rpn("3 2 -")
    verify_answer(1, answer)


@pytest.mark.functest
def test_subtract_negative(calculator):
    answer = calculator.calculate_rpn("2 3 -")
    verify_answer(-1, answer)


@pytest.mark.functest
def test_multiply(calculator):
    answer = calculator.calculate_rpn("2 3 *")
    verify_answer(6, answer)


@pytest.mark.functest
def test_divide(calculator):
    answer = calculator.calculate_rpn("3 2 /")
    verify_answer(1, answer)


@pytest.mark.functest
def test_divide_zero(calculator):
    answer = calculator.calculate_rpn("0 2 /")
    verify_answer(0, answer)


@pytest.mark.functest
def test_divide_invalid_zero(calculator):
    answer = calculator.calculate_rpn("2 0 /")
    verify_answer(None, answer)


@pytest.mark.functest
def test_modulo(calculator):
    answer = calculator.calculate_rpn("3 2 %")
    verify_answer(1, answer)


@pytest.mark.functest
def test_modulo_zero(calculator):
    answer = calculator.calculate_rpn("0 2 %")
    verify_answer(0, answer)


@pytest.mark.functest
def test_modulo_invalid_zero(calculator):
    answer = calculator.calculate_rpn("2 0 %")
    verify_answer(None, answer)


# negative integer test cases
@pytest.mark.functest
@pytest.mark.parametrize(
    "input, expected",
    [
        ("2 4 * -8 +", 0),  # valid rpn notation
        ("2 5 * 4 + -3 2 * -1 + /", -2),  # valid postfix(rpn) notation
        ("2 15 * 4 + -3 2 * - 45 %", 40),  # valid postfix(rpn) notation
    ],
)
def test_negative_input_calculations(calculator, input, expected):
    answer = calculator.calculate_rpn(input)
    verify_answer(expected, answer)


# mix of valid and invald test cases
@pytest.mark.functest
@pytest.mark.parametrize(
    "input, expected",
    [
        ("2 4 * 8 +", 16),  # valid rpn notation
        ("2 4 * 8 + 9", None),  # invalid rpn notation
        ("2 4 % 8 + 9", None),  # invalid rpn notation
        ("2 +", None),  # invalid length
        ("2 + 3", None),  # valid infix notation
        ("2 + 9 +", None),  # invalid infix notation
        ("+ 2 3", None),  # valid prefix notation
        ("+ b 3", None),  # invalid notation
        ("% 2 a", None),  # invalid notation
        ("2 4 * o +", None),  # invalid notation
        ("2 4 * P +", None),  # invalid notation
        ("2.2 4.8 * P +", None),  # invalid notation
        ("2.0 4.0 * 8 +", None),  # invalid notation
    ],
)
def test_mix_input_calculations(calculator, input, expected):
    answer = calculator.calculate_rpn(input)
    verify_answer(expected, answer)


# complex functions test cases
@pytest.mark.functest
@pytest.mark.parametrize(
    "input, expected",
    [
        ("10 6 9 3 + -11 * / * 17 + 5 +", 22),
        ("2 5 * 4 + 3 2 * 1 + /", 2),
    ],
)
def test_complex_input_calculations(calculator, input, expected):
    answer = calculator.calculate_rpn(input)
    verify_answer(expected, answer)


# validate input strings test case
@pytest.mark.inputvaildation
@pytest.mark.parametrize(
    "input, expected",
    [
        ("2 4 * 8 +", True),  # valid rpn notation
        ("2 5 * 4 + 3 2 * 1 + /", True),  # valid postfix(rpn) notation
        ("2 +", False),  # invalid length
        ("- +", False),  # invalid length
        ("2 + 3", True),  # valid infix notation
        ("2 + 9 %", True),  # invalid infix notation
        ("_ 2 3", False),  # valid prefix notation
        ("% b 3", False),  # invalid notation
        ("+ 2 a", False),  # invalid notation
        ("2 4 * o +", False),  # invalid notation
        ("2 4 * P +", False),  # invalid notation
        ("2.2 4.8 * P +", False),  # invalid notation
        ("2.0 4.0 * 8 +", False),  # invalid notation
    ],
)
def test_is_valid_notation(calculator, input, expected):
    answer = calculator.parse_inputs(input)
    verify_answer(expected, answer)

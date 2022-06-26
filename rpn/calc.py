"""
calc.py contains logic to evaluate rpn expression
"""


import logging
from dataclasses import dataclass, field
from typing import List, Union

from rpn.calc_func import add, modulo, subtract, multiply, divide


@dataclass
class Calculator:
    """Calculator class"""

    operator: List[str] = field(default_factory=lambda: ["*", "/", "+", "-", "%"])

    def calculate_rpn(self, input: str = "") -> Union[int, None]:
        """Calculate the answer for given input string in reverse polish notation

        Parameters
        ----------
        input : str, required
            Input string representing reverse polish notation, by default ""

        Returns
        -------
        Union[int, None]
            Result can be either input (for valid input rpn notation) or None (for invalid input rpn notation)
        """
        if self.parse_inputs(input):
            input_token = input.split(" ")
            st = []
            for x in input_token:
                # if only operators extract top two entries on stack and perform operation x
                if x in self.operator:
                    if len(st) < 2:
                        logging.info("Not a valid reverse polish notation")
                        return None
                    op1, op2 = st.pop(), st.pop()
                    if x == "+":
                        res = add(op1, op2)
                    if x == "-":
                        res = subtract(op2, op1)
                    if x == "*":
                        res = multiply(op1, op2)
                    if x == "/":
                        res = divide(op2, op1)
                        if res is None:
                            return None
                        else:
                            res = int(res)
                    if x == "%":
                        res = modulo(op2, op1)
                        if res is None:
                            return None
                    st.append(res)
                # else push to stack
                else:
                    st.append(int(x))
            if len(st) == 1:
                return st[0]
            else:
                logging.info("Not a valid reverse polish notation")
                return None
        else:
            logging.info("Invalid Input")
            return None

    def parse_inputs(self, input: str = "") -> bool:
        """Verify whether the input string is a valid prefix/postix/infix notation

        Parameters
        ----------
        input : str, required
            Input string representing any of prefix/postix/infix notation, by default ""

        Returns
        -------
        bool
            True if input is a valid prefix/postix/infix else False
        """
        input_token = input.split(" ")
        # input should at least contain 3 input tokens i.e. 2 operands and 1 operation
        if len(input_token) < 3:
            logging.info("Invalid input length")
            return False
        # input should contain only characters from operator and digits lists
        if any(
            [
                False
                if x in self.operator or x.isdigit() or x.lstrip("-").isdigit()
                else True
                for x in input_token
            ]
        ):
            logging.info("Invalid character found")
            return False
        return True

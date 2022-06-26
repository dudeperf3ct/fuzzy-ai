"""
streamlit_app.py contains streamlit application for calculating RPN
"""

import streamlit as st

from rpn.calc import Calculator


def main(calc):
    st.title("Reverse Polish Notation Calculator")
    st.write("")

    user_expr = st.text_input(label="Please enter a expression")
    if len(user_expr) != 0:
        if not (calc.parse_inputs(user_expr)):
            st.error(
                "Invalid Expression! Please try again with a valid expression. See logs for more info!"
            )
        else:
            output = calc.calculate_rpn(user_expr)
            if output is None:
                st.error(
                    "Invalid RPN! Please try again with a valid RPN. See logs for more info!"
                )
            else:
                st.success(f"{output}")


if __name__ == "__main__":
    calc = Calculator()
    main(calc)

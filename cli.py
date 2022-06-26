"""
cli.py contains logic to create a command line interface for the calculator
"""


import typer

from rpn.calc import Calculator


def main(
    input_text: str = typer.Option(
        ..., help="Input Reverse Polish Notation expression to evaluate"
    ),
):
    """Create a CLI using typer

    Parameters
    ----------
    input_text : str, required
        Input string, by default typer.Option( ..., help="Input Reverse Polish Notation expression to evaluate" )
    """
    calc = Calculator()
    if input_text:
        typer.secho(f"Input Expression: {input_text}", fg=typer.colors.MAGENTA)
        if not (calc.parse_inputs(input_text)):
            typer.secho(
                "Invalid Expression! Please try again with a valid expression.",
                fg=typer.colors.RED,
            )
        else:
            output = calc.calculate_rpn(input_text)
            if output is None:
                typer.secho(
                    "Invalid RPN! Please try again with a valid RPN.",
                    fg=typer.colors.red,
                )
            else:
                typer.secho(f"Answer: {output}", fg=typer.colors.GREEN)


def run():
    typer.run(main)


if __name__ == "__main__":
    run()

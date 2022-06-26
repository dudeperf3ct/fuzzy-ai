from setuptools import setup

setup(
    name="rpn",
    version="0.1.0",
    author="dudeperf3ct",
    packages=["rpn", "tests"],
    entry_points={
        "console_scripts": ["calc = cli:run"],
    },
    license="LICENSE.md",
    description="RPN Calculator command line tool",
    long_description=open("README.md").read(),
    install_requires=[
        "typer >= 0.4.1",
    ],
)

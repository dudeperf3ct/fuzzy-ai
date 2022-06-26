# Fuzzy Labs Technical Test

Write a command line program that accepts an RPN expression as input and evaluates it. The calculator should support the following operations:

- Addition (+), Subtraction (-) and Multiplication (*)
- Integer Division (/),
- Remainder or modulo (%)

The calculator should only accept whole numbers as inputs and it should only output whole numbers.

## Run Locally

Pre-requisites:

- [Docker installed](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script)

Build a docker image

```bash
docker build -t rpn -f Dockerfile.dev .
```

Run the docker container in background.

```bash
docker run -t -d -p 8501:8501 --name calc rpn
```

### Pytest

Run tests using `pytest`.

```bash
docker exec calc python3 -m pytest -v --cov
```

### Streamlit

A simple prototype using streamlit.

```bash
docker exec calc streamlit run streamlit_app.py
```

### Typer CLI

[Typer](https://typer.tiangolo.com/typer-cli/) is a library for building CLIs (Command Line Interface applications).

```bash
python3 cli.py --help
python3 cli.py --input-text "2 3 +" 
```

### Docker container

Inside a docker container, we can test all above again.

Remove previous running docker container with name `calc`.

```bash
docker rm calc
```

```bash
docker run -it -p 8501:8501 --name calc rpn
```

```bash
# run tests using pytest
python3 -m pytest -v --cov
# test application using streamlit
streamlit run streamlit_app.py
# test using typer
python3 cli.py --help
python3 cli.py --input-text "2 3 +" 
```

### Command Line

Either inside docker container (recommended) or on your system

```bash
pip install -e .
```

```bash
calc --help
calc --input-text "2 3 +"
```

## Additional Questions

1. How would you implement an infix notation calculator, i.e. ordinary arithmetic expressions such as `1 + 2`, on top of your RPN calculator?

    The easiet way to implement a infix notation calculator reusing RPN calculator will be to add a extra functionality which converts infix notation to postfix notation.

2. How would you deploy your calculator as a service in a cloud environment?

    Basic: If we just want to expose our application as a service, we can create a lambda function which exposes a endpoint that takes in an input string and provides an answer.

    Advanced: If we want to create a application i.e. a cool calculator with fancy UI we can deploy this on EC2 instance. If our fancy application starts to get more traffic, we can make the whole architecture a bit flexible by adding transitioning application to a kubernetes cluster, giving us ability to scale-in and scale-out.

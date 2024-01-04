# hsouli_parsing
Coding assignment - Logging parsing

## Prerequisites
- Python >= 3.9
- Poetry >= 1.7.1 (`pip install poetry`)

## Setup
```shell
poetry install
```

## Launch
````shell
python -m parsing_assignment LOG_FILEPATH
````

## Tests
Unit tests are provided, you can run them using:
````shell
pytest ./tests
````
or with coverage:
````shell
pytest --cov=parsing_assignment ./tests
````

## Container
You can test the code using a Dockerfile:
````shell
docker build -t coding_assignment .
docker run coding_assignment
````
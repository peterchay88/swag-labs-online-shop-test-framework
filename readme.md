# Online Shop Test Framework

This test framework is designed to test the functionality of the swag labs
[online shop.](https://www.saucedemo.com/) This framework will leverage selenium 
via python. The framework will be built using pytest and dependencies will be 
managed using poetry.

## Requirements
- Python 3.12.5
- [Poetry](https://python-poetry.org/docs/) installed on your machine

Navigate to the root of the project directory and run the below command to install the projects 
dependencies 
```commandline
poetry install
```

### How To Run Tests
In order to run the tests you will need to use the pytest command. Optional arguments are test number and browser.
By default the browser is chrome and if no test number is defined then all tests will be run. When specifying a
test number use the `-m` argument to signal it.
```commandline
pytest -m <test number> --browser <browser>
```

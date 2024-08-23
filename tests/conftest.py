import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def my_driver(request):
    if request.config.getoption("--browser") == str.lower("chrome"):  # Not sure if the lower argument does anything
        driver = webdriver.Chrome()
    elif request.config.getoption("--browser") == str.lower("firefox"):
        driver = webdriver.Firefox()
    else:
        raise TypeError(f"Invalid value. Expected chrome or firefox but got {request.config.getoption('--browser')}")
    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Please specify which browser to test on")

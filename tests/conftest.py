import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def my_driver(request):
    if request.config.getoption("--browser") == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.config.getoption("--browser") == "firefox":
        my_driver = webdriver.Firefox()
    else:
        raise TypeError(f"Invalid value. Expected chrome or firefox but got {request.config.getoption('--browser')}")
    yield my_driver
    my_driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Please specify which browser to test on")

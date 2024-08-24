from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element(self, element: tuple) -> WebElement:
        """
        Method for finding element on webpage
        :return: Returns a web element
        """
        return self.driver.find_element(*element)

    def _enter_text_into_element(self, element: tuple, text: str):
        """
        Method for entering text into a web element
        :return:
        """
        self._find_element(element).send_keys(text)

    def _click_button(self, element: tuple):
        """
        Method for clicking web elements
        :return:
        """
        self._find_element(element).click()

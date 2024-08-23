from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element(self, element: tuple):
        """
        Method for finding element on webpage
        :return:
        """
        self.driver.find_element(element)

    def click_button(self):
        pass

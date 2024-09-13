from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging as logger


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _wait_until_element_is_visible(self, element: tuple, time: int = 10):
        """
        This method waits a specific amount of time to see if a web element is visible on the page
        :param time: Specified time to wait
        :param element: Web element locator
        :return:
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.visibility_of_element_located(element))

    def _wait_until_element_is_clickable(self, element: tuple, time: int = 10):
        """
        This method waits until an element is clickable on the web page
        :param time: Specified time to wait
        :param element: Web element locator
        :return:
        """
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.element_to_be_clickable(element))

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
        try:
            self._wait_until_element_is_clickable(element)
            self._find_element(element).click()
        except NoSuchElementException:
            logger.error(f"Error element with locator {element} is not clickable")

    def _is_displayed(self, element: tuple, time: int = 10) -> bool:
        """
        This method checks to see if the web element is displayed.
        :param element: Web Element
        :return: True or False
        """
        try:
            self._wait_until_element_is_visible(element, time)
            return self._find_element(element).is_displayed()
        except NoSuchElementException:
            return False


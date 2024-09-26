from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
import logging as logger


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"
    __login_button = (By.CLASS_NAME, "submit-button")
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __login_error_msg = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = self.__url
        super().__init__(driver)

    def get_current_url(self) -> str:
        """
        Returns the current URL of the page
        :return:
        """
        return self.driver.current_url

    def check_current_url(self) -> bool:
        """
        Checks the current url and validates it against the login page URL
        :return:
        """
        if self.get_current_url() == self.__url:
            return True
        else:
            return False

    def open_login_page(self):
        """
        This method opens the login page
        :return:
        """
        logger.info(f"Opening web page: {self.__url}")
        self.driver.get(self.__url)

    def enter_username(self, username: str):
        """
        This method enters the username into the username field.
        :param username: Username to enter
        :return:
        """
        logger.info(f"Entering \"{username}\" into the username field.")
        super()._enter_text_into_element(element=self.__username_field, text=username)

    def enter_password(self, password: str):
        """
        This method enters the password into the password field.
        :param password: Password to enter
        :return:
        """
        logger.info(f"Entering \"{password}\" in the password field.")
        super()._enter_text_into_element(element=self.__password_field, text=password)

    def click_login_button(self):
        """
        This method clicks the login button
        :return:
        """
        logger.info("Clicking login button")
        super()._click_button(element=self.__login_button)

    def execute_login(self, username: str, password: str):
        """
        This method logs into the Swag labs online shop
        :return:
        """
        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def check_login_error_exists(self) -> bool:
        """
        This method checks to see if the login error is thrown when invalid credentials are used
        :return:
        """
        logger.info("Checking to see if login error exists")
        return super()._is_displayed(element=self.__login_error_msg)

    def check_login_error_message(self) -> str:
        """
        This method returns the login error text
        :return:
        """
        if self.check_login_error_exists():
            return super()._find_element(element=self.__login_error_msg).text
        else:
            raise NoSuchElementException





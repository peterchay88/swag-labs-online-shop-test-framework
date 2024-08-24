from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"
    __login_button = (By.CLASS_NAME, "submit-button btn_action")
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(driver)

    def open_login_page(self):
        """
        This method opens the login page
        :return:
        """
        self.driver.get(self.__url)

    def enter_username(self, username: str):
        """
        This method enters the username into the username field.
        :param username: Username to enter
        :return:
        """
        super()._enter_text_into_element(element=self.__username_field, text=username)

    def enter_password(self, password: str):
        """
        This method enters the password into the password field.
        :param password: Password to enter
        :return:
        """
        super()._enter_text_into_element(element=self.__password_field, text=password)



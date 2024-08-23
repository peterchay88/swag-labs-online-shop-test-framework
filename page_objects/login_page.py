from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    __url = "https://www.saucedemo.com/"
    __login_button = (By.CLASS_NAME, "submit-button btn_action")
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_login_page(self):
        """
        This method opens the login page
        :return:
        """
        self.driver.get(self.__url)

    def enter_username(self, username: str):
        """
        This method enters the username into the username field.
        :param username:
        :return:
        """
        self.driver.find_element()



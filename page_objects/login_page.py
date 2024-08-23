from selenium.webdriver.common.by import By


class LoginPage:
    __url = "https://www.saucedemo.com/"
    __login_button = (By.CLASS_NAME, "submit-button btn_action")
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")

    def enter_username(self, username: str):
        """
        This method enters the username into the username field.
        :param username:
        :return:
        """
        pass

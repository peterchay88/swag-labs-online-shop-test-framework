import pytest
from page_objects.login_page import LoginPage
import logging

pytestmark = [pytest.mark.login, pytest.mark.positive]


class TestLoginPagePositive:

    def test_login(self, my_driver):
        """
        This test confirms that we can log into the swag labs online shop
        1. Enter Username, 2. Enter Password, 3. Click login, 4. Validate successful login
        :return:
        """
        login_page = LoginPage(driver=my_driver)
        login_page.open_login_page()
        login_page.enter_username(username="standard_user")
        login_page.enter_password(password="secret_sauce")

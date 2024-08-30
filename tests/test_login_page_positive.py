import pytest
from page_objects.login_page import LoginPage
import logging as logger

pytestmark = [pytest.mark.login, pytest.mark.positive]


class TestLoginPagePositive:

    @pytest.mark.parametrize("username, password, test_id", [
        pytest.param("standard_user", "secret_sauce", "1", marks=pytest.mark.tcid01),
        pytest.param("visual_user", "secret_sauce", "2", marks=pytest.mark.tcid02)
    ])
    def test_login(self, username, password, test_id, my_driver):
        """
        This test confirms that we can log into the swag labs online shop
        1. Enter Username, 2. Enter Password, 3. Click login, 4. Validate successful login
        :return:
        """
        logger.info(f"Running test {test_id}")
        login_page = LoginPage(driver=my_driver)
        login_page.open_login_page()
        login_page.enter_username(username=username)
        login_page.enter_password(password=password)
        login_page.click_login_button()

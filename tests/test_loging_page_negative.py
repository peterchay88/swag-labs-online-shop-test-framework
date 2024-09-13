import pytest
import logging as logger
from page_objects.login_page import LoginPage

pytestmark = [pytest.mark.login, pytest.mark.negative]


class TestLoginPageNegative:

    @pytest.mark.parametrize("username, password, test_id", [
        pytest.param("incorrect_user", "secret_sauce", "3", marks=pytest.mark.tcid03),
        pytest.param("standard_user", "incorrect_password", "4", marks=pytest.mark.tcid04),
        pytest.param("incorrect_user", "incorrect_password", "5", marks=pytest.mark.tcid05,)
    ])
    def test_incorrect_credentials(self, username, password, test_id, my_driver):
        """
        This tests confirms we met the expected error when entering the incorrect credentials on the login page
        1. Open webpage, 2. Enter in incorrect username + Password combo, 3. Click login,
        4. Verify that the correct error message is displayed on the webpage
        :return:
        """
        logger.info(f"Running test {test_id}")
        login_page = LoginPage(my_driver)
        login_page.open_login_page()
        login_page.enter_username(username=str(username))
        login_page.enter_password(password=str(password))
        login_page.click_login_button()
        # Confirm login error is correct
        error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.check_login_error_message() == error_msg, \
            f"Error, unexpected error message. Expected {error_msg}. Actual {login_page.check_login_error_message()}"
        
